let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
	silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
	autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
elseif empty(glob(data_dir . '/undodir'))
	silent execute '!mkdir -p ' . data_dir . '.vim/undodir'
endif

call plug#begin('~/.vim/plugged')

Plug 'arcticicestudio/nord'
Plug 'altercation/vim-colors-solarized'
Plug 'vim-airline/vim-airline'
Plug 'lervag/vimtex'
Plug 'thaerkh/vim-workspace'
Plug 'valloric/youcompleteme'
Plug 'mbbill/undotree'
Plug 'xuhdev/vim-latex-live-preview'
Plug 'scrooloose/nerdtree'
Plug 'jeffkreeftmeijer/vim-numbertoggle'
Plug 'zhamlin/tiler.vim'
Plug 'alvan/vim-closetag'

call plug#end()

" configure expanding of tabs for various file types
au BufRead,BufNewFile *.py set expandtab
au BufRead,BufNewFile *.c set expandtab
au BufRead,BufNewFile *.h set expandtab
au BufRead,BufNewFile Makefile* set noexpandtab

set noerrorbells
set novisualbell
" Tohle opravdu funguje
set belloff=all

" Helps force plug-ins to load correctly when it is turned back on below.
filetype off

set textwidth=120
set tabstop=4 softtabstop=4 shiftwidth=4
set expandtab
set autoindent
set smartindent
set smartcase
set noswapfile
set undodir=~/.vim/undodir
set undofile
set incsearch
set mouse=a
set ruler
set showcmd

" toggle hybrid line numbers
" set nu
set number relativenumber

" vim-workspace
let g:workspace_autosave_always = 1

" make backspaces more powerfull
set backspace=indent,eol,start

set list listchars=tab:\|\ ,trail:·,extends:>,precedes:<,nbsp:%
set list

set numberwidth=5
highlight LineNr ctermfg=grey ctermbg=Black

syntax on

nmap <leader>n :NERDTreeFocus<CR>
nmap <C-n> :NERDTree<CR>
nmap <C-t> :NERDTreeToggle<CR>
nmap <C-f> :NERDTreeFind<CR>

nmap <F8> :TagbarToggle<CR>

nmap <silent> <A-Up> :wincmd k<CR>
nmap <silent> <A-Down> :wincmd j<CR>
nmap <silent> <A-Left> :wincmd h<CR>
nmap <silent> <A-Right> :wincmd l<CR>

imap jk <Esc>
imap kj <Esc>
