for pkg in $(cat ./assets/pkgs/aur_pkgs); do
  banner
  echo "[*] Installing AUR package '$pkg'..."
  sleep 2
  yay -S --noconfirm --answerdiff=None $pkg
  sleep 2
done
yay -Sc --noconfirm

banner
