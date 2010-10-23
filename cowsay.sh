cows=($(cowsay -l))
ncows=${#cows[@]}
let ncows=ncows-4
let random=RANDOM%ncows
let random=random+4
fortune -s | cowsay -o -s -f ${cows[random]}
