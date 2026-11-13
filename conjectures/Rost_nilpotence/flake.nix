{
  description = "Code tools (SageMath, Python) for this conjecture's proofs runs";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      lib = nixpkgs.lib;

      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAllSystems = f:
        lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});

      pythonPackages = ps: with ps; [
        sympy
        networkx
        numpy
      ];

      toolsFor = pkgs: {
        python = pkgs.python3.withPackages pythonPackages;
        sage = pkgs.sage.override { requireSageTests = false; };
      };

      lockPkgs = nixpkgs.legacyPackages.x86_64-linux;
      lockTools = toolsFor lockPkgs;
    in
    {
      devShells = forAllSystems (pkgs:
        let tools = toolsFor pkgs; in {
          default = pkgs.mkShell {
            name = "proofs-code-tools";
            packages = [ tools.python tools.sage ]
              ++ lib.optionals pkgs.stdenv.isLinux [ pkgs.bubblewrap ];
          };
        });

      proofsTools = {
        tools = {
          sage.version = lockTools.sage.version;
          python = {
            version = lockPkgs.python3.version;
            packages = lib.listToAttrs (map
              (p: lib.nameValuePair p.pname p.version)
              (pythonPackages lockPkgs.python3Packages));
          };
        };
  
        # The most bytes a script's RESULT line may hold.
        policy.result_bytes = 65536;
      };
    };
}
