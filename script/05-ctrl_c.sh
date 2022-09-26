ctrl_c () {
  echo -e "\n[-] Process cancelled by user. Exiting...\n"
  tput cnorm; exit 1
}
trap ctrl_c INT
