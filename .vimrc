call plug#begin('~/.vim/plugged')

Plug 'arcticicestudio/nord-vim'
Plug 'vim-airline/vim-airline'
Plug 'lervag/vimtex'
Plug 'thaerkh/vim-workspace'
Plug 'valloric/youcompleteme'
Plug 'mbbill/undotree'
Plug 'xuhdev/vim-latex-live-preview'
Plug 'scrooloose/nerdtree'

call plug#end()

set noerrorbells
set novisualbell
" Tohle opravdu funguje
set belloff=all

" Helps force plug-ins to load correctly when it is turned back on below.
filetype off

set tabstop=4 softtabstop=4 shiftwidth=4
set smartindent
set nu
set smartcase
set noswapfile
set undodir=~/.vim/undodir
set undofile
set incsearch

" vim-workspace
" autocmd BuffWritePost *.tex !pdftex
let g:workspace_autosave_always = 1

colorscheme nord

syntax on

nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
