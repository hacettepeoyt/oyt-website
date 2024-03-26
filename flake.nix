{
  description = "";

  # Nixpkgs / NixOS version to use.
  inputs.nixpkgs.url = "nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    with nixpkgs.lib;

    let
      version = "2.2";

      # System types to support.
      supportedSystems = [ "x86_64-linux" "aarch64-linux" ];

      forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);

      nixpkgsFor = forAllSystems (system: import nixpkgs { inherit system; overlays = [ self.overlay ]; });

    in {

      # A Nixpkgs overlay.
      overlay = final: prev: {

        oyt-website = with final; final.callPackage ({ inShell ? false }: stdenv.mkDerivation rec {
          name = "oyt-website-${version}";

          src = if inShell then null else ./.;

          buildInputs = with pkgs; [
            python311
            python311Packages.django
            python311Packages.django-crispy-bootstrap5
            python311Packages.django-crispy-forms
            python311Packages.django-simple-captcha
            python311Packages.pillow
            python311Packages.requests
          ];

          installPhase =
            ''
              mkdir -p $out
              cp -r . $out
              echo "#! ${stdenv.shell} -e" > $out/run-oyt-website
              echo '${python311}/bin/python $(readlink "$0")/oytwebsite/manage.py runserver'
              wrapProgram $out/run-oyt-website --prefix PYTHONPATH : "$PYTHONPATH"
            '';
        }) {};

      };

      packages = forAllSystems (system:
        {
          inherit (nixpkgsFor.${system}) oyt-website;
        });

      defaultPackage = forAllSystems (system: self.packages.${system}.oyt-website);

      # Provide a 'nix develop' environment for interactive hacking.
      devShell = forAllSystems (system: self.packages.${system}.oyt-website.override { inShell = true; });

      # A NixOS module.
      nixosModules.oyt-website =
        { pkgs, ... }:
        {
          nixpkgs.overlays = [ self.overlay ];

          options.services.oyt-website = {
            enable = mkOption {
              type = types.bool;
              default = false;
							description = ''
								Enables oyt-website service.
							'';
            };

						
          };

          config = {
						systemd.services.oyt-website = {
							enable = mkIf cfg.enable true;
							wantedBy = [ "multi-user.target" ];
							after = [ "network.target" ];
							startLimitBurst = 3;
							startLimitIntervalSec = 60;

							serviceConfig = {
								ExecStart = "${pkgs.oyt-website}/run-oyt-website";

								Restart = "always";
								WorkingDirectory = "${pkgs.oyt-website}";
								User = "oyt-website";
								Group = "oyt-website";
								Type = "simple";

								LockPersonality = true;
								PrivateDevices = true;
								PrivateTmp = true;
								PrivateUsers = true;
								ProtectClock = true;
								ProtectControlGroups = true;
								ProtectHome = true;
								ProtectHostname = true;
								ProtectKernelLogs = true;
								ProtectKernelModules = true;
								ProtectKernelTunables = true;
								ProtectProc = "invisible";
								RestrictNamespaces = true;
								RestrictRealtime = true;
								RestrictSUIDSGID = true;
								SystemCallArchitectures = "native";
								UMask = "0027";
							};
            };
          };
        };
      };
}
