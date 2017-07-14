Put everything in ~/.bashrc
then add this line to ~/.profile and ~/.bash_profile

[ -r $HOME/.bashrc ] && source $HOME/.bashrc
