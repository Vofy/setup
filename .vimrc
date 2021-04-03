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

call plug#end()

set noerrorbells
set novisualbell
" Tohle opravdu funguje
set belloff=all

" Helps force plug-ins to load correctly when it is turned back on below.
filetype off

set tabstop=4 softtabstop=4 shiftwidth=4
set smartindent
set smartcase
set noswapfile
set undodir=~/.vim/undodir
set undofile
set incsearch
set mouse=a

" toggle hybrid line numbers
" set nu
set number relativenumber

" vim-workspace
let g:workspace_autosave_always = 1

set list listchars=tab:⟶\ ,trail:·,extends:>,precedes:<,nbsp:%
set list

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
