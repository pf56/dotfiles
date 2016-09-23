execute pathogen#infect()

syntax on
filetype plugin indent on

set encoding=utf-8
set number

" tabs appear 4 spaces wide
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smarttab

" solarized
set background=dark
colorscheme solarized

" airline
let g:airline_powerline_fonts = 1
let g:airline_theme='solarized'

" syntastic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" python
let python_highlight_all=1
