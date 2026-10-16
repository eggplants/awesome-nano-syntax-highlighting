# awesome-nano-syntax-highlighting

[![release](
  <https://github.com/eggplants/validate-ubuntu-autoinstall-docker/actions/workflows/release.yml/badge.svg>
)](
  <https://github.com/eggplants/validate-ubuntu-autoinstall-docker/actions/workflows/release.yml>
) [![Awesome](
  <https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg>
)](
  <https://github.com/sindresorhus/awesome>
)

A curated collection of [GNU nano syntax highlighting files](https://www.nano-editor.org/dist/latest/nanorc.5.html#SYNTAX%20HIGHLIGHTING).

## Usage

```sh
echo 'include "/path/to/nanorc/files/*.nanorc"' >> ~/.nanorc

# optional
echo 'include "/path/to/nanorc/files/_extras/*.nanorc"' >> ~/.nanorc
```

## Lists

### Official

- [nano.git/tree/syntax](https://git.savannah.gnu.org/cgit/nano.git/tree/syntax)
  - [Unofficial GitHub Mirror](https://github.com/madnight/nano/tree/master/syntax)
  - 1999-2026
  - `asm,autoconf,awk,c,changelog,cmake,css,default,email,go,groff,guile,html,java,javascript,json,lua,makefile,man,markdown,nanohelp,nanorc,nftables,objc,ocaml,patch,perl,php,po,python,ruby,rust,sh,sql,tcl,tex,texinfo,xml,yaml`
  - extras: `ada,fortran,haskell,povray,spec`

### Large vault

- [galenguyer/nano-syntax-highlighting](https://github.com/galenguyer/nano-syntax-highlighting) (actively maintained fork of scopatz/nanorc)
  - 2022-2026
  - `Brewfile,Dockerfile,Rnw,apacheconf,arduino,asciidoc,asm,awk,batch,beancount,brainfuck,c,clojure,cmake,coffeescript,colortest,conf,conky,creole,csh,csharp,css,csv,cython,d,dot,dotenv,elixir,email,erb,etc-hosts,expect,fish,fortran,fsharp,gemini,genie,gentoo,git,gitcommit,glsl,go,godot,gophermap,gradle,groff,haml,haskell,hcl,html,html.j2,i3,ical,ini,inputrc,jade,java,jrnl,js,json,jsonc,jsx,julia,keymap,kickstart,kotlin,ledger,lisp,lua,m3u,makefile,man,markdown,moonscript,mpdconf,mutt,nanorc,nginx,nmap,ocaml,octave,patch,peg,perl,perl6,php,pkg-config,pkgbuild,po,pov,powershell,privoxy,prolog,properties,pug,puppet,python,reST,rego,rpmspec,ruby,rust,scala,sed,seed7,sh,sieve,sls,solidity,sparql,sql,subrip,svn,swift,systemd,tcl,tex,toml,ts,twig,v,vala,verilog,vhdl,vi,x11basic,xml,xresources,yaml,yum,zeek,zig,zsh,zshrc`

- [scopatz/nanorc](https://github.com/scopatz/nanorc) (unmaintained; see galenguyer/nano-syntax-highlighting)
  - 2010-2020
  - `Dockerfile,Rnw,apacheconf,arduino,asciidoc,asm,awk,batch,c,clojure,cmake,coffeescript,colortest,conf,conky,creole,csh,csharp,css,csv,cython,dot,dotenv,elixir,email,erb,etc-hosts,fish,fortran,fsharp,gemini,genie,gentoo,git,gitcommit,glsl,go,gophermap,gradle,groff,haml,haskell,hcl,html,html.j2,i3,ical,ini,inputrc,jade,java,javascript,js,json,keymap,kickstart,kotlin,ledger,lisp,lua,m3u,makefile,man,markdown,moonscript,mpdconf,mutt,nanorc,nginx,nmap,ocaml,octave,patch,peg,perl,perl6,php,pkg-config,pkgbuild,po,pov,powershell,privoxy,prolog,properties,pug,puppet,python,reST,rego,rpmspec,ruby,rust,scala,sed,sh,sieve,sls,sparql,sql,svn,swift,systemd,tcl,tex,toml,ts,twig,vala,verilog,vi,x11basic,xml,xresources,yaml,yum,zig,zsh,zshrc`

- [serialhex/nano-highlight](https://github.com/serialhex/nano-highlight)
  - 2011-2024
  - `Dockerfile,apache2,apacheconf,aptsrclist,asm,bash,batch,c,c-file,changelog,changelogs,clike,coffee,conf,config,config2,config3,configfiles,conky,css,cython,default,delphi,desc,dotemacs,dotenv,dummy,ebuild,editorconfig,ekghistory,emailquote,etc-stuff,etcportage,etcxml,fortran,gentoo,groff,haskell,havp,html,httpstatuscodes,info,ini,initng,initscript,java,js,lex,lisp,log-stuff,lua,maincf,makefile,man,markdown,mimetype,mutt,named,nanorc,nscd,others,paludis,passwd,patch,perl,php,php2,plaudis,po,pony,postgresql,pov,privoxy,python,rcfiles-new,reST,rsync,ruby,scheme,sh,shlike,softcam,sourceslist,tab,tcl,tex,todo,toml,txt2tags,urls,vhdl,xdefaults,xml,xorg,yacc,yaml`

- [Naereen/nanorc](https://github.com/Naereen/nanorc) (marked deprecated by the author)
  - 2017-2024
  - `apache2,apacheconf,asm,awk,c,c-file,caml,changelog,changelogs,clike,cmake,conf,config,config2,config3,configfiles,conky,css,cu,cython,debian,default,delphi,desc,dotemacs,dummy,ekghistory,etc-stuff,etcxml,fortran,gentoo,groff,haml,havp,histoire,html,info,initng,initscript,java,js,julia,log-stuff,lua,maincf,makefile,man,markdown,mgp,mimetype,mutt,named,nanorc,nscd,objc,others,paludis,passwd,patch,perl,php,php2,pkgbuild,po,postgresql,pov,privoxy,profile,python,rcfiles,rcfiles-new,reST,rsync,ruby,sh,shlike,softcam,sources_list,strips,tab,tcl,tex,urls,vhost,xdefaults,xml,xorg,zshrc`

- [gerph/nano-colour](https://github.com/gerph/nano-colour)
  - 2026-2026
  - `arm,bash,bbcbasic,c-file,cmhg,codeowners,default,fish,fortran,git-commit,git-rebase,git-tag,go,graphviz,groovy,html,jfpatch,jinja2,js,json,lua,makefile,markdown,nanorc,obey,pascal,perl,php,python,terraform,xml,yaml`

- [pazmivaniye/nanorc](https://github.com/pazmivaniye/nanorc)
  - 2024-2026
  - `bash,c,cabal,cython,default,erlang,f90,glsl,haskell,html,ini,json,julia,makefile,matlab,metal,nanorc,nasm,objc,paz,pbm,php,powershell,python,rust,tcl,tex,toml,yaml`

- [hroskes/nanorc](https://github.com/hroskes/nanorc)
  - 2014-2023
  - `Dockerfile,c,cython,fortran,groovy,html,ini,javascript,json,markdown,matlab,nanorc,perl,python,sh,sql,tex,yaml`

- [richrad/nanorc-mac](https://github.com/richrad/nanorc-mac)
  - 2012-2012
  - `awk,c,css,emacs,email,html,ini,javascript,kickstart,lua,main,makefile,man,markdown,nanorc,nginx,patch,privoxy,python,rpmspec,ruby,sed,sh,sql,systemd,vala,xml,yaml`

### Small vault

- [minilux-org/nanorc-minilux](https://github.com/minilux-org/nanorc-minilux)
  - 2026-2026
  - `minilux`

- [rfanth/tjson-highlight](https://github.com/rfanth/tjson-highlight)
  - 2026-2026
  - `tjson`

- [ogswag/org-syntax-for-nano](https://github.com/ogswag/org-syntax-for-nano)
  - 2026-2026
  - `org`

- [njjenkins/stata-nanorc](https://github.com/njjenkins/stata-nanorc)
  - 2026-2026
  - `stata`

- [njjenkins/R-nanorc](https://github.com/njjenkins/R-nanorc)
  - 2026-2026
  - `R`

- [aaron-dotnet/nanorc-extras](https://github.com/aaron-dotnet/nanorc-extras)
  - 2026-2026
  - `csharp`

- [StevieEngbrock/english.nanorc](https://github.com/StevieEngbrock/english.nanorc)
  - 2026-2026
  - `english`

- [Noiseko/nano-nix](https://github.com/Noiseko/nano-nix)
  - 2026-2026
  - `nix`

- [Kapendev/zen-c-nanorc](https://github.com/Kapendev/zen-c-nanorc)
  - 2026-2026
  - `zc`

- [0hip/nanorc-for-FANUC](https://github.com/0hip/nanorc-for-FANUC)
  - 2025-2026
  - `fanuc`

- [nousantx/javascript-nanorc](https://github.com/nousantx/javascript-nanorc)
  - 2024-2026
  - `js,ts`

- [ursalang/nanorc-ursa](https://github.com/ursalang/nanorc-ursa)
  - 2023-2026
  - `ursa`

- [gerph/nanorc-riscos](https://github.com/gerph/nanorc-riscos)
  - 2020-2026
  - `arm,bbcbasic,c-file,cmhg,jfpatch,obey`

- [hankache/raku.nanorc](https://github.com/hankache/raku.nanorc)
  - 2018-2026
  - `raku`

- [cqn-brwpna9/uiua-nano-config](https://github.com/cqn-brwpna9/uiua-nano-config)
  - 2025-2025
  - `uiua`

- [cadeweinberg/nanorc](https://github.com/cadeweinberg/nanorc)
  - 2025-2025
  - `zig`

- [GitHubonline1396529/nano-zimpl](https://github.com/GitHubonline1396529/nano-zimpl)
  - 2025-2025
  - `zimpl`

- [uuupah/nanorc](https://github.com/uuupah/nanorc)
  - 2025-2025
  - `jsonc`

- [distant-chervony/nano-keyd-syntax-hl](https://github.com/distant-chervony/nano-keyd-syntax-hl)
  - 2025-2025
  - `keyd`

- [AntoineLandrieux/SoareLanguageSupport](https://github.com/AntoineLandrieux/SoareLanguageSupport)
  - 2025-2025
  - `soare`

- [remisalmon/nanorc](https://github.com/remisalmon/nanorc)
  - 2022-2025
  - `bash,csv,default,dockerfile,env,fish,go,json,log,lookml,markdown,python,sql,terraform,toml,tsv,xml,yaml`

- [tramegit/calcpad-nano](https://github.com/tramegit/calcpad-nano)
  - 2024-2024
  - `cpd`

- [ysdragon/ring-nano](https://github.com/ysdragon/ring-nano)
  - 2024-2024
  - `ring`

- [tdeshazo/fountain_nanorc](https://github.com/tdeshazo/fountain_nanorc)
  - 2024-2024
  - `fountain`

- [sls1005/kotlin-nanorc](https://github.com/sls1005/kotlin-nanorc)
  - 2024-2024
  - `kotlin`

- [procedium/sacalon-nanorc](https://github.com/procedium/sacalon-nanorc)
  - 2024-2024
  - `sacalon`

- [kabirdkng/pact-nano-syntax](https://github.com/kabirdkng/pact-nano-syntax)
  - 2024-2024
  - `pact`

- [jxpx666/blackbox-syntax-highlight](https://github.com/jxpx666/blackbox-syntax-highlight)
  - 2024-2024
  - `blackboxmenu,blackboxmenu-copiar2,blackboxrc,blackboxrc-copiar2,blackboxrcfile,blackboxsessionmenufile,desktop,dot,dotenv,email,keymap,man,mutt,x11basic,xresources`

- [duyqphung/fsharp-nanorc](https://github.com/duyqphung/fsharp-nanorc)
  - 2024-2024
  - `fsharp`

- [danburk10/inform6.nanorc](https://github.com/danburk10/inform6.nanorc)
  - 2024-2024
  - `inform6`

- [Wsoum/loza-nanorc](https://github.com/Wsoum/loza-nanorc)
  - 2024-2024
  - `loza`

- [SteveHH72/yaml-erweiterung-nano](https://github.com/SteveHH72/yaml-erweiterung-nano)
  - 2024-2024
  - `yaml`

- [NicRiv/nanorc](https://github.com/NicRiv/nanorc)
  - 2024-2024
  - `vhdl`

- [Mrezadwiprasetiawan/Java-nanorc](https://github.com/Mrezadwiprasetiawan/Java-nanorc)
  - 2024-2024
  - `default,sunset,vibrant`

- [Tech-Matt/nano-vhdl](https://github.com/Tech-Matt/nano-vhdl)
  - 2023-2024
  - `vhdl`

- [sls1005/nim-nanorc](https://github.com/sls1005/nim-nanorc)
  - 2022-2024
  - `nim`

- [Oples/nanorc-nim](https://github.com/Oples/nanorc-nim)
  - 2019-2024
  - `nim`

- [sls1005/cython-nanorc](https://github.com/sls1005/cython-nanorc)
  - 2023-2023
  - `cython`

- [sls1005/R-nanorc](https://github.com/sls1005/R-nanorc)
  - 2023-2023
  - `R`

- [markusmueller73/purebasic.nanorc](https://github.com/markusmueller73/purebasic.nanorc)
  - 2023-2023
  - `purebasic`

- [emacstheviking/mercury-nano-mode](https://github.com/emacstheviking/mercury-nano-mode)
  - 2023-2023
  - `mercury`

- [R-Rothrock/assembler-nanorc](https://github.com/R-Rothrock/assembler-nanorc)
  - 2023-2023
  - `asm`

- [sith-ikjetil/pascal.nanorc](https://github.com/sith-ikjetil/pascal.nanorc)
  - 2020-2023
  - `pascal`

- [davidhcefx/Nano-Syntax-Highlighting_Batch-File](https://github.com/davidhcefx/Nano-Syntax-Highlighting_Batch-File)
  - 2020-2023
  - `bat`

- [tomkyle/nanorc-brewfile](https://github.com/tomkyle/nanorc-brewfile)
  - 2019-2023
  - `Brewfile`

- [sami2020pro/pashmak-nanorc](https://github.com/sami2020pro/pashmak-nanorc)
  - 2021-2022
  - `pashmak`

- [lejun/wiki.nanorc](https://codeberg.org/lejun/wiki.nanorc)
  - 2022-2022
  - `wiki`

- [lejun/cooklang.nanorc](https://codeberg.org/lejun/cooklang.nanorc)
  - 2022-2022
  - `cooklang`

- [serjan-nasredin/toit.nanorc](https://github.com/serjan-nasredin/toit.nanorc)
  - 2021-2021
  - `toit`

- [nyrLang/nyrLang-syntax-nano](https://github.com/nyrLang/nyrLang-syntax-nano)
  - 2021-2021
  - `nyr`

- [sami2020pro/vile-nanorc](https://github.com/sami2020pro/vile-nanorc)
  - 2021-2021
  - `vile`

- [bfu4/solidity-nanorc](https://github.com/bfu4/solidity-nanorc)
  - 2021-2021
  - `solidity`

- [megidont/quakec-nanorc](https://github.com/megidont/quakec-nanorc)
  - 2020-2021
  - `qc`

- [mwsoverdick/bitbake_nanorc](https://github.com/mwsoverdick/bitbake_nanorc)
  - 2020-2020
  - `bb`

- [CraftTweaker/zenscript-nanorc](https://github.com/CraftTweaker/zenscript-nanorc)
  - 2020-2020
  - `zs`

- [Nuolong/bminor-nano-syntax-highlighting](https://github.com/Nuolong/bminor-nano-syntax-highlighting)
  - 2020-2020
  - `bminor`

- [poison4999/odin-nano-syntax](https://github.com/poison4999/odin-nano-syntax)
  - 2020-2020
  - `odin`

- [GutPuncher/holyc-nano](https://github.com/GutPuncher/holyc-nano)
  - 2020-2020
  - `hc`

- [vinesworth/d-nanorc](https://github.com/vinesworth/d-nanorc)
  - 2013-2020
  - `d`

- [megasaturnv/openscad-nano-syntax-highlighting-nanorc](https://github.com/megasaturnv/openscad-nano-syntax-highlighting-nanorc)
  - 2019-2019
  - `openscad`

- [tomkyle/nanorc-conf](https://github.com/tomkyle/nanorc-conf)
  - 2019-2019
  - `conf`

- [pic16f874/isc-nanorc](https://github.com/pic16f874/isc-nanorc)
  - 2018-2019
  - `isc-cos,yaml`

- [loglob/csharp.nanorc](https://github.com/loglob/csharp.nanorc)
  - 2018-2019
  - `csharp,csharp.colorful`

- [i137/bash-nanorc](https://github.com/i137/bash-nanorc)
  - 2018-2018
  - `sh`

- [Martinfx/nanorc](https://github.com/Martinfx/nanorc)
  - 2018-2018
  - `gnucobol`

- [ccie5022/cisco.nanorc](https://github.com/ccie5022/cisco.nanorc)
  - 2018-2018
  - `cisco`

- [IanChew/ARM-assembly-nanorc](https://github.com/IanChew/ARM-assembly-nanorc)
  - 2017-2018
  - `arm`

- [mitchell486/nanorc](https://github.com/mitchell486/nanorc)
  - 2015-2018
  - `bat,powershell,sh`

- [AndrewGilchrist/custom_nanorc](https://github.com/AndrewGilchrist/custom_nanorc)
  - 2017-2017
  - `c,ftl,java,mako,perl,xsd`

- [paw-lu/toml-nanorc](https://github.com/paw-lu/toml-nanorc)
  - 2017-2017
  - `toml`

- [Rah1x/nanorc](https://github.com/Rah1x/nanorc)
  - 2017-2017
  - `_ALL,css,ini,logs`

- [krupski/intel-hex.nanorc](https://github.com/krupski/intel-hex.nanorc)
  - 2016-2017
  - `intel-hex`

- [Selonka/wdl_nanorc](https://github.com/Selonka/wdl_nanorc)
  - 2016-2016
  - `wdl`

- [faissaloo/gml.nanorc](https://github.com/faissaloo/gml.nanorc)
  - 2016-2016
  - `gml`

- [defaye/git.nanorc](https://github.com/defaye/git.nanorc)
  - 2016-2016
  - `git`

- [SimonItaly/pawn-nanorc](https://github.com/SimonItaly/pawn-nanorc)
  - 2016-2016
  - `pawn`

- [indrajithbandara/Naxe](https://github.com/indrajithbandara/Naxe) (copy of the removed my-old-projects/Naxe)
  - 2016-2016
  - `haxe`

- [mbentley/Dockerfile.nanorc](https://github.com/mbentley/Dockerfile.nanorc)
  - 2015-2015
  - `Dockerfile`

- [devrimgunduz/nanorc-pgsql](https://github.com/devrimgunduz/nanorc-pgsql)
  - 2014-2015
  - `pgsql`

- [gregoswald/whileyHighLightingInNano](https://github.com/gregoswald/whileyHighLightingInNano)
  - 2014-2014
  - `whiley`

- [borjaeg/nanorc](https://github.com/borjaeg/nanorc)
  - 2014-2014
  - `javascript,python,sh`

- [danielpclark/nanorc-erb](https://github.com/danielpclark/nanorc-erb)
  - 2014-2014
  - `erb,ruby,yaml`

- [serianox/lua.nanorc](https://github.com/serianox/lua.nanorc)
  - 2013-2013
  - `lua`

- [matiasinsaurralde/golang.nanorc](https://github.com/matiasinsaurralde/golang.nanorc)
  - 2013-2013
  - `go`

- [sebastianwagner/dar.nanorc](https://github.com/sebastianwagner/dar.nanorc)
  - 2013-2013
  - `dar`

- [domix/nanorc](https://github.com/domix/nanorc)
  - 2012-2012
  - `groovy`

- [mikelietz/feature.nanorc](https://github.com/mikelietz/feature.nanorc)
  - 2011-2012
  - `feature`

### Archived

Read-only on GitHub; still usable but no longer updated.

- [jamesrweb/elm.nanorc](https://github.com/jamesrweb/elm.nanorc)
  - 2022-2022
  - `elm`

- [le-jun/cooklang.nanorc](https://github.com/le-jun/cooklang.nanorc) (GitHub mirror of lejun/cooklang.nanorc)
  - 2022-2022
  - `cooklang`

### Removed

The following repositories listed in 2022 no longer exist.

- talia9tailz/nanorc (`mumps`)
- bitskitn/nutc-nanorc (`nutc`)
- my-old-projects/Naxe (`hx`; a copy remains at [indrajithbandara/Naxe](https://github.com/indrajithbandara/Naxe))
- i-tsvetkov/nanorc (`todo,url`)
