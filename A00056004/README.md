# Sistemas Operacionales - Parcial 2
**Nombre:** Brayan Andrés Henao  
**Código:** A00056004  
**Correo:** bryanhenao96@gmail.com  
**URL Repositorio:** https://github.com/brayanhenao/so-exam2
___

## Instalación y configuración de zsh y git
Para la instalación y configuración de zsh y sus plugins se siguen los siguientes pasos:
Los comandos utilizados para la instalación mediante apt-get requieren permisos de usuario root (sudo) por lo que se tiene como prerequisito que el usuario sea sudoer o ya se esté como root en la terminal al momento de ejecutar el comando.

1- Se instala zsh con el siguiente comando:
```console
apt-get install zsh
```

2- Una vez instalado zsh, cambiamos al usuario operativos previamente creado, exportamos una nueva variable de entorno para asegurarnos de no instalar zsh en el directorio root y se hace un llamado curl para terminar la instalación. Se utilizan los siguientes comandos en el orden explicado previamente:
```console
su operativos
export ZSH="$HOME/.dotfiles/oh-my-zsh"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

Pdta: Si no se tiene curl, se instala con el siguiente comando:
```console
apt-get install curl
```

3- Para configurar el accesso a git mediante un token personal, se utiliza el siguiente comando:
```console
 config remote.origin.url "https://bb6e9c33977eec34df142484d9cfd372084ce488@github.com/brayanhenao/so-exam2.git"
```

## Instalación y configuración plugin zsh-autosuggestions

1- Se instala el plugin con el siguiente comando, el cual clona el repositorio del plugin al directorio de zsh:
```console
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

2- Una vez instalado, se debe adicionar al archivo de configuración de zsh con un editor de texto la siguiente línea:
```console
nano ~/.zshrc
plugins=(git zsh-autosuggestions)
source ~/.zshrc
```

3- Para configurar finalmente el color subrayado en el autocompltado, se crea el siguiente archivo y se adiciona una línea con el nuevo color:
```console
nano $ZSH_CUSTOM/soexam.zsh
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=yellow"
source ~/.zshrc
```

## Instalación y configuración de Tmux

1- Se instala Tmux utilizando el siguiente comando:
```console
apt-get install tmux
```
2- Para configurar los keybinds de Tmux se modifica el siguiente archivo:
```console
nano ~/.tmux.conf
```
