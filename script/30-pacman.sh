for pkg in $(cat ../assets/pkgs/official_pkgs); do
  banner
  echo "[*] Installing official package '$pkg'..."
  sleep 2
  sudo pacman -S --noconfirm $pkg
  sleep 2
done

banner
