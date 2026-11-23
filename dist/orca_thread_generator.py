# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-thread-studio"
# name = "Orca Thread Studio"
# description = "Offline threaded containers, caps, adapters and mechanical fasteners"
# author = "Orca Thread Studio"
# version = "1.1.0"
# ///

# MIT License
#
# Copyright (c) 2026 Orca Gear Studio
# Copyright (c) 2026 Orca Vase Studio
# Copyright (c) 2026 Orca Thread Studio
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import sys as _orca_init_sys
import types as _orca_init_types
if __name__ not in _orca_init_sys.modules:
    _orca_init_sys.modules[__name__] = _orca_init_types.ModuleType(__name__)

# ===========================================================================
# MODULE: thread_studio.language_packs
# ===========================================================================

"""Discover data-only offline language packs in source, wheels and standalone bundles.

This module is self-contained so future Studio plugins can use the same format
without importing another plugin. Catalogs never contain executable code.
"""
pass  # [bundled] hoisted __future__ import

import base64
import json
from pathlib import Path
import re
import zlib

_BUNDLED_LANGUAGE_PACKS = json.loads(zlib.decompress(base64.b85decode('c-q~a`;**6mhb-+g?|{>7(aLn%mj}6Lt`7mVuP>S1H1FfhPo=dTDYoITT&UiHzvZ}jc0g{85mwOybK0Ezy=luY%oK_)_<}^b=yD9{S)r@oRgVKNhy`u(4M_F0^Cw6m6=Lqo^$f#r;h$(#~|Ht-+$~#T1%=I{@V#POrp5I<Gwq0?r6nrwc|dzzH>)EOrsO(-}+&Xl8(f~bkrG*FDAIuj)tn0@=ZIs=@2RLu&stW?z>~>j&vCIlWs^?6RPE?N))Q2ziBuchLro*(olu%WM|Nd`)L^U(SjiCw}Y@94pKV#udjnaI7H3qFlq&Dl|&t?>u8*`LfkfpQ<Vft@`vqssN|Mm{DewlxpjPj?u}8~5h)4f(sP8v@%vP6Ob>Eos7^%cNu)m(C8Mw#t%T!q;}7Vr15XX`$haa0HvI@y(n^DFw19_MMuz*Ng>HlvwL-MiG=fT>4^Pm!?tuBQdm<c~^PM~Pt1cSF6|}mei2CJ$C=GOb4)p(h6t<<i=AMeeZjjh6--q_#;VG4BX${qrK`+)9(MSJ2QheW|1J#fE9VE^zD7?O5X!}0s#-o9vP74c#9~uq#ITpKNzZG-8CW;^4)_6GVQo9d_ttIM_2QZ2_;eqkRo}xMq^gCfk^;AE_YYn^0Nkm;g*B_thMv0=*RlgNRPbuVmB<@AX6AZ&PHKf%=+fg%@7k4|MxzLw<xZ@DDf1ri|US8ZC>2}YZ2>au6c=_=#Kyn)D{%kAsLOTiKey|*mhQVUg4Ry;<$}s9<VC)W#&_U1&`K?lk0TMb%u%H$(x`K2G9m37T*h+V!x<}0;=nC*Rwq?f{o9!@&di1iBco^;u9>Q_d3xk+O`uIYWP%r5Ebno_QP~)}%x;vEWcFXWhdE`<u4=Yp`&@jg=qe+MEJ`vH#LdOMR&{IjMUw)u?>;{W*m!~Jj!7!qXn2P)s@<V%H-0x!?DBCZ%<01PDG+A*Ka}HVWKK#Ia!9Br~VYiF<cn_L0*s~C)Y1|9C;j)>}cn0b_8E~A8o~FkMLUd|4#Eb5rwlJj*M#JJ^)Zt#nH18_vW?c^+O+gA!O|7tpCUEzm(s<88h!Lf9GWVM9h$I-YxY!-cCDNx!kWfdrqXeR1VKlx(<siSJ>Ox!lZkhcG?+foT?A{k7c$3{|G2)(y@s`!zV6cQ?jr&k#8sK$~`Vgd?XLs;Oj5&jM+wbh;`JRmMxEPm<aopZDLVG(S8sw?sXUx}yV^m<PY(c#3wPS5@d<m7tL7$%E1ZrsG^6p?>^@0wU81Z{Oq1y6Nb@h}x9tEQWqpT}64R`b0llhtQgD5;fH-=Q;cfY8HN~R%|Zj#0q`z_SbkF(rV!uV1uvi9*XO7Ylu(jiZpM~AI&z8keLTbJU5XU-fwd>g|9ZQ?|lIa$8lnOMdI|91#R%nB+>^btn=2ybb3z~ehzLeD4Zs2#;<Vy+ZagohtrIKf?Fr>NX6g`wv#A?W=>oZ_GHH&jl)*qWmx3GNH-4E6+f;s3jlBZcZrg8voVvHQ+Dkc2<K;y-uY8}xc2>M+IKd-(0@n|8`gJLRUGaueqDXoz`-(ZLFr&lH*+?&^`8oL>qDA{2)`mTfA8L{|x`*4Aj4XoZG1l}%ftvPk8y4ADoB;n4Km;2`F&VkL$n3_>0~e2Gi@c|a-*SLuMXmsV<4n~`$rc5!+vZu1@g9Ez4D1x*qq9MI{pus2}QHK!Fkby23fap8VQY^|Qd#gRPAVMq^BGisEW=MR2{*^BX;h;<>IVH3xH<+8Mf`x%B$lIaJw9c-czd56OUvi?{1lA6O^UG#lOvz6vZ!a6Ry-c#*}BnI+D+&;<5gOl%l0<$VOs9?@$6=H^OFYJ#<x5fR%2o0u-d-*mkO^~w(GbkZ}Y(>Ftes)p?F&jKw2S#krQATB`r=pIs#Y&pgwU=%ZNrFE}Q!P~}UDV^xM252#5gGF{BW<bEQ<m003m%L*3yO`EJ`6nS1)IhLcQF)EF``Pxms*j^^of2~I8#sQS9CB;jw|Tfr4Tu2{Oltsk`rBKFry-6OtEZK+f<v`Xhlcj9Pum2!%&cUnPbhpU^f&_X7df@Ji9u7>`?A1okP{4px{6cucg}#=A-U$7MjpT2NFpPxh@)-3OcU^JsAf3pb+W771^VZzk#_H@~}+t!XICX@GmUymg-`7h!sx9&{_ABk%VW#6Vmh<j*=y4r+x8&45Rypaesy0ha4bz0ps*Q(uz-D#v%XzdG}AB1pl(@Xt)ds^f(4UaQiW~+ea;oj(@_Poa1O1#k>9mS&s0CFqy{Rw4!$WPxR!_d3c8%v||w5{$HQ{6Hgg2Ani3y_taTY3uk@hbg<t}bdjl?xDWl4h`7YPAKFT!Ea!aZj{kn)_26+#zr~@fVCWo{>k{?vK^4;)U>Qmy8CcWzAv%#+)IkPWL4>T;&_jEI2fA@Q6d^^ufrL??yVKaP<2P`1{Dxzz8cmi-t>E@vkGg5U6<KWaX-&l!ZTqnHiL(c^9hx<c7b;Mz!2{azB$;T9P`W~c4syNU>9VT8@%a6IXC(6d(UG1XPvLJrWPyDmN|!Oa%(GGgj0_SB=4l_mpyG;PAn@or77thj3}Tk#WChaLgJDLm;jOjcF|0n=#L&x(;P!u|E}%=Yma!RbKO#cwUuDF+{C)5s%(4|)CU%401PM)7e%HA2KuG3}d)?`9^;Ao#cA}*$n=jU6VMQqYP1*2pF)bNJy@J(F3XA$G92Qhbrb1x-a0XhIL~R&ZX%g}B#x8({sv~!?5+uVYq*^GMjZw+W{rHe$cZpF9>t+xqksY6TBaBwme7(3fO_%v0k41ynS(0X|QL7zZRB(4A6C2C={XrwqI>#(J=yHdw^+n3?h)gGpd3X7SH5#w6SyA?QeCu_#nGO1iS<Vh37*RI&kuXX00@LO*D^>JQn&sRV^Gb>bIJX&++}t7R%F$9tdk~hUYNM|bmdY@Z+cHes%XN)LsjYZ8$jaVlTonP9DxIa&-ZR&wl{MRzq@_)MmKoXOvBWUfcyif`Jg@Av{oJOZyA;lH@`AW+bL4xpDu2FLMQhV3n$3ziOW}1hn^5X0GA?Nh@llwikumMO4h*?Pv|nTd#&s(BvzMsv8o~q*Q?XVDDy1Q-MPF)bc#vNAo}fQUS@10I*xN%Z`j)+1(fL@N>ini+vM7TETD)idEbn!oZA_c>p*}n@Hk%$h_9}#=dwD*jbz^q*1Zntg-6&1t)am~N{n{Z-rqzIkT2g2p%o{cU`g-Xut<2h2xSnt`GgGTGjAJ(3#nNI^$hEZ&^7Y`!sO>cDP&n-9vE2&YDXeqX4TXwZpm3eeq?Jot&byB++71mH68PGM^~5M4n`@DzKKB)MjWK?W-QLcx5BAB`n7jcc^Ie<v_rYX-0@Kk51IOyW4~a$~z(9|Ox!dqS>8!g*(udJXzB<!X7J<1N2P_7;rE%__)Rl#~TUy!R$w{f7!$aBDOEH|Jq<u2+-h#b`nWkFDt!COoGQJabsh9`jL>X_ayH=x-)gzS$Z%t?>+0XTiHETB{m?`_f{=>m9?)k6JX!e;yS~#(3bMGB|;jp%|<Qz(D-=n+k{ME1S%q>@_cyGGtq+i}q%<oU%Sy<BXtMDxJhO&A!y+fK#I_seAq&snTC;r}rzju*OjQmyXFMxz%WinI|oAZa%B72g_Gdtv2`EY+U?5eg*0Vu5qcBvRwurfFu^Awgor_J{;(&()piW1I)#g=5^BgyojdWsd?Q)zfY1jFMpaqf?Y3o#@_XiLIiK#y<%RASH?f7usX^8RqRzzrQl9kW308W)~jME7!z-{RFp;{}FifXxU!5uX^z5IsVEP?+913xiCwRx}WYw!)-tm$JZigmf97fi+8=U3S(|_g6SqJ%)<UM9CW`d9$QwkoZlJqGjQ=DLmFh$&Sz#gtZ-v)nM!ezok&N5z5v<-Y&2ffi(n*s=ivu=XJ7A8@qbgqk)Zb%e1c5XI9gebgWOi=JaZ%MlGm0kAf?xwkoAoP-i7YW_Ne8-5<TllWqST(TkE~x!+pCiYi)x=Q!_hPcSF=3OZ&tuL{Mrge4%H{7e6R@*|Q*NFw{OM@w5uBKevu1*1V5s|qfXSG`zJ$Oe~`g>@3%LcS<TE0%@^k?(_?Sy*sj8urt@*gnFp3~q)i)Tm&o>j>*EntxF*^Uu)ID`HPJgdLVXdV$JrY~#LyBbyhi@G!`xMTjK|m-zs<pN*aq5$CefTIGD_HO7G1$>~`4oGbLb#i)|iVD@Mf`{44{K&kG$Rk1T~F6`9npRiw{)O8CA_Q%e$X|Yoq4a&6yv<Z=z!QifjlhJ_s7cIoJ!b}bpM(vKmJ4K`6{?X0ZldX7Z=YmF}qMeq^W}$atm(SQ$AYT<Z@WvNtEw2(OaE08LPRsT<{#V+Q2uGAmMet+fMB|e(>EUor$SXfe!Ud=sw&{6w%+i>;b#K<besMh-56y!;>B>{PUQ^WcKDBa@q*Gsdm3x;&`d+7n?b4DK51=11)Lzrf$=#^=cndJx_qt8YbvHRR9bJ;O-EMt*9)P8t)=1&rVhi)Vo*PemBgxYJ`^cFc{NfH{KvD|McCus*;bNf6cm2v-Zb@oPNl;wz@OZKm4>;2=Z5i-6w5XxKq;ifNI2Ke|dX?8aW;FKShDn;6J#4=PJmR7u4XMY%)@alV?xuap;2vuA94wq6ci-Lj$YSW8Um3giF3xuMU0kNNbt#dv-A$I>;a}X5y+5CsJd{m%yr;w5YlrW}d+*AgbHP|vVk`%T@1=Zq-W4oSrsMs1LFyl08o*l@;0j&8>kf>l#dH^EdXgkCmFt$bV9dRMGAl7T*<4_XB5>R{JO`|AXkNC_<};7|yfUlw*lv%Bea2#8-zeq1B5G$WGQUNFC9{+qH&_N3%xf2`^?cd6#*Neh+DdBlaN^rvU=iFVwICVUQqVgQhASa~jk&}drOXkGl0qSraeSc{V02*G(<b5xf)vE;hGq^hs(IJZZixF*ckcK#nPm4-A1{V0oN`og%28z!4$)XbcaV-pNA?89Q2aLJFZ=yz7fzNh`VazTl*YS`!p>n_<RHd0CNP|=<1>2KRkrm4gX%bEFrF3{$#;x@X~U<h61{PvRcj&Tx4+%FL-p(FAY3ofK>$8Lb}ZGQL3h@oL2MG;EEaTg_m#mQbK-JA=BNY&c~PKZN|^!5&Kv?rALIZadsyaw^5-Q2D0k{oK;~#R1XO?BA%MCn2LQ=I6#(Q*tp$K8FI7Q6zSM2SfVQn@hx_5b9_*)(P=Wk-68)r4IqjBXKHFT+KN9QN&bpd{JWX;nLU?9o`Kb_|pQ4nT0(iE3ix=O~XBoUBe{=ATJ<Q-8`P+=!$)6XHofFChcKA$i9s1Y8I{e47I{c?h>WE%6n2!9-5FPqcf#`S=s}LPu>edjQ^7UJU>1=ZqMOMc>^HDm*lsuy&M;<=Mo_PqJLV}0RDJ0Y*In~$vEKVJXQ^(<y(|i<8F{PTo@u$}jIKK481Wrv3KYde9t08Z4X?565KJn(*o9w)bzwxD(;G5iO0ljff>d>32D;3<0C$UW3<j+gcjXuth8~IxS+&Bp?ZWBw%hPKJUHgYf%xA9(@N!oa>Y=N|CkgWo=@g&aXZ0fH!r)>P!OOQ?O)I-=55{iJ0dzP^^VLe+@alwz)l+&uv8eggd)#!r)QsbOdQ8m8Q8la})LIJ69PD((Hb5;-3R9~xxYW(T-V2z}dxf)f;)%a3<G)*z3K+!lSet@Q&=0j(SDMe<+Ju4A2xzkEw#+&TLWlBkTL?$~furba_8H>rESMV^N#0nP1lURYkcoO{pOgU{f|5AUwAp=vm)C_^iUulTH6fQLbVDeXd2uv}>Pr;PaN*qk?v_QW&Ck?q5=j?w5^&+W;d!c_V_40`H$1LPU{#xLL|G2P=IdV7`ec(_o`k=(Qa4x}I=wA!CJT7yg#I_U?EZxF?ie!s>Rwi5W=XtaxJ1(;=?x_cCDI`==E#*`%&{9e&@+|IInP)jxm`O#FC4cUPSV~D2W6^623$bYH)(^4xQhgvxF{KI2l0PpZEbdtzUdfI#YDNA!%!)qnFe`<G0<hwolpvMdX$ertotC(i+-aFg$)8t4DgN|IBBhk*VN!DEbv#PGoUPF)TgmNbPs(Yxh(2jp%yuIvH(%KHp(oo>?Dlgf+gtv&Vkg^HbOAMSPCTSZA;HI)6jQdFGjXr@Fq2|RnJ~$pSE41}WFJ>jOz|)!x$`=vr0PnMC2`NZ97!R?i;$F(>M4@yYcnB|+RKd@l9`!q3LyElpuH9z;WLLEv4=Ouj<{z(IX05az($fXHj)g&@#k^3jvKjaMo1Y*Ao&IFj}0n=`lCUlnDAUKhL%Ch2!)o;3@vlUA6kZfr$^_ZC$P-0Sx}i}T=ztkImp2jm@5wH7cwdrSw_&nLTDNDOPUkZE)QOUnb?ZPU-YXY%pB-5tyPFHGx%{4W(rkSg_wCz^%jORL(Iqz0I;D0G@=*jpT^X1CJ%y#Ck%WGp=Mf2BF&7{wuhQI&<*6(W^pW3*NHW=Ob^>NKU{U9%^;P-%|u=LoBbq0ceP=eaVy6CiZA30CD(<V3Hj!3*qRY>2BT%5axrJP4Ye_6{wIZ;8BpvP!UiJ}2z#RbqCQ0D%T?;TL=e%g6ME(lC2}v))^Ccjh(1b2{||(m(L>HeoWXAqbif%5;dz`$yqWPOd8v>j2w0`)XA)9B53zofk2xdoe#59UQQu9X-)i@1v>|`oJ;C&{jXV=J!&abf^p7P_uSA|v+Y))^P$<Gx3w<dKj{#QO6M#n905n{h>i-n+XL!!LH}ys|=C%-j2ESCokK`e4W`&=bYqe;$Mx_8WP(H&V#v;S2G6IbrPd#4<8m;Owq$Nx62BA5cDReg!O~Xhu$Ks)MqJz1NFU2!L(JW_)Gh@*#>qH|8Z!#8*>?_|2%7u4SyN;oxL(*Wliy<wF#g2AUg(RE6G^(2k9KiMXSJ9NL2VUkx8Z9@AO|x7bn<lCZO=DhJb!-~?1!GtpmxiBmxv1b8#HC>^+T*A+>J~($QM04c%ne%@`}9M<t;D2R=yFV&-t3q(ymDF~s32&m0adlNur$lCXDDI}kA~p(Gz&`;&I(Hd?Ex!q1qIBGOOvbSN5!RiOxIe$#>~N%TNtYP$TZqSo*kNo&f^~&nTDr>HV<>ktPYhikJ&gx4U}Hglb2r%Q**{2rbd2+UlpeY^KUV(4O25WMC`xNWoPCV;Mtsw&e&zq2^*}Y2|FVJZkBE;N=?y@&_B0>1eI_#ef>L2Eqv<Z)flV4dAu45SA$;<g?bdA{h?=FwFRC=j5r&%#)!!3ur<8sy{Wi0yr5~5b23#BFS)oiGSliJ*PPi><eFxIYYxTzP6QLr{4nn)jas7{OcqrOuWT!EYw{YsI($tPY!f$)USn3-&EwaYJGKzPhS%da9m0mAiZ+a3)3Oq>CW6fh#nnjhMrKB^QT&_vmAU{nkJ4ff)$%(_wS9WCQEX@_H;c)!Lw05e8=I3?_$f@t*dM^=fLyEzVdLaTxRoAS=O}DR=`>@Ld3l{V>{jZ0L%E}A0GsMt^7IZ|-;jkXS{i!psv~(Ir%8_XMgKL9Wz)_7EM43G4WrqdF~25X-byqZD_-z;<4ao!XS2m<Hr;}d^zuB}!j1#m)Wo&nur?5g-G)(Z%0X?+GLULA)A;|7s5Wj;n|-E>X2!IE9&ar<F>M}N;l*AdsLf&e1+pqcw3*}B7+Vf$gMY(LEJmv)eh$Nx1OuWjqRkhch&JI(#j{y5E@v0|fvW+tuWP+~9`=VVkoveboJHc=gtNlhc%8VFac$1bjB8UJ*5*)o4tiqRlq`<=s5Ut(qY&K2#e(9x*fu2#!V3lEtcI<|xAExn^0R1FT>yl<>Uma(8?E3<xKLj87I7h;x-El4CG}Su-o}^BU_@1F&KKxL?>Xgmr0Rp+Y$4W7KZ|zLt&Vns#R@i9w-)ZEdsE?V=3~<8`c3GFH?q)@h&Lfeyy@`sS%28D3N|`09Evu=&G0qeGS(>c*c5K8oBl0{b`#RVwqT;{v^K|1u_l%?6Jgt9+#CvJV93@FHxK&_6@hN3RNb;Yj$b#3b+8q_ogU#9phkyutQQ*_230SOpnmio3U{bp)#swz6kdT1b7P+{w7#%y#Eq((Pm)#3I}>qjZ?SFp9&hI~mA<#g9XSSNb)Xw3)2whePF7MUyv1=#!`?KBdQ%(nMk3y9A>2)?F4&DVqL;N1?T>bIB<{@)bYsivX(N#1+(g<8^#;0G7|NEp<52PiyJ^`Keb;Qp)knKA)WXbwH`;Mn@SVBdt448eA_;rbzuCYyhqNS<f+#EPM`IhAv+$QMW=6lUYI>OQ29hnzg~3@0Tlp|JCZRSAj_QRCNhUhb9!(nxCoC~dxtE`rBLX+gvq~Q7z$-<>30ojb*r7Fv7~Y9+PSK2yXGP_YXFY^T4Ci)S$2r|y!#PE?FAG~J{1KQFJz<(gav!K27^snaLJRvod?H`af|@j+&{9>HlU&L{PID-fzi^ZzoY=q#y@1mp9Pt-Nbe)m^gIRP+b`^ZaD>OYlcvFFH;s>gMo46Q+_Ddp(Ra2mw=1!cDpshE@Hff<BK|W(SvJ?s3RIJnDO&CT|TnM3~pQ(y)3JGwcA>F+#Y(bn1vT(>Xh||F+hW?Zb)`U>Ch|`MRqoIo(38c1-l+&U7(?D@+)+y{3zN^I+8OJk5Re(|WFhBsRfI{ZtPdhRdOTWvPw^#_Mm6cd3R{3vht*k^o&gmht;saheV_3zNloP5TL!b8=pgefkQ{_<w;xupCkLd{O0AbMnL5LGcgnQ7P^pY&%6j{QFM1;PGY9k&CbjY#<oEi6M#B39EU)(3}WRPc@Zh7FH`K&5+pRRxkFmzK&bW?7uEk^QHt(Z6WbS6|wHNpI3)M<r2jugQ+0Fx%v&EU}$=NYH1#N*NBXUQw{RR>ILsP3psYZxvjYW{JphoBF!P0uI+%3;W9TL`DyLL=}ou_450UotAwO*AifAszpe(Rt>0p1b$J7{EPSgPSndp+6e1O$0YNXw$rjrJe(u93>U`=_dKW7Nbqw$n$lr!pF5TtZ5|LQDaT;Xp$)6A~L9H5S5@Nt=Ao<>9L3lvQc|fR8KRhEHSEtnZ&Rl(Tx5@vQg7p!kMB(w%9^`tXl#zCFB~zkX_LI8H?k?!I?yR*x^l;(6_X7rI1-s*NPXK3CNr{vd2R)<)n_%0@%wk9TCSd$=@xrOnnheQ6<d87BNILiA~t@`h}ISCaqa%A)aY8HG^p?XiSosbx4yGTtPIMi*-N~u4|qtuH%_HIi9Hj&?H1t#6(j(5W>0kGh1X`VFW_Z4MJEM=#MQSO`T3;StB%vm?p|pPc-4}Bnx2|8hAF$l&_$cX8PYFiq~6BGtE<-RV>p{+8dAA^IZWm;aH|t$1p?{BvYzpqfDw9%M=Bf!m1;f<k7O0)#FP{FQu_J-j7IV%PuAKiLJOY;?MX!%=9w46z9;TZd&}pR?-MulHNAll4=GnncFCX<WO5;mmCX0`%j~;{mfRRE%-`gDN`i@_hrb;&MamL6I0Q;onm2=@hXc20hgknxLj&ZF0GJ}CWeflOPS2{pi7ZmM|;sFtugeEICQoGzC=q2Eu?7y5Mgz*rEhPAIR~z4^6f2IoX&!nM*YqbO#V<e9qX1d$7FPuhhs|WD5lWaQf&O~Ep80mlIihEhACA)8e)=lwB3N59WF?2DE4k0!-TbVln0ndvDD&AXg-S&88Ip4uj7{@;+NP`b?+$hOUHP$?+MywH{J^`nf_<(nxwTK;ELt#GEtgV#}exB2QaG8rC%r5aGQ-T*@4O%sHzrTvU#a-{7Vd&johJLgekk+#!5|ETcViUOe1cxhhv%-B*JWwmrSzCuW~Ip-JUpw%;cN$Bc<ln!iT!ZV{PA_@3vadX$v8X_KB4ZM}jIX3z{)bq1iu##UtT5no&+h{6tm{Z{?d^yq-uKb53PB>P4OIw?ggb=r^t0s&OaC%suQ;^5agjB2?_fNk<ED5q5ekVx&q>_~t>3;>MJdyFO|{IeGKfQcnCHT+E5d6vH{iO))2OdS#RowhAJhl0i<ti8@ep^3E;fWM*^`a%x3+%xNAgxfZ|pjC4AX2<W6T(rFHK02X~hFqc>-j2G(st|?x_PDg0f)QNk&GVo*;>%D^KxtwFsI-+yj6Zs;7NZfwDk9m=Q)k06o|1~elljvk_LpAl}^XFDUPX(K&>SJEk318x#ymPXQJ{8TBO7N*{n&iQ!R5d1_ie`rwe9D;`jln06?cgJyih92IX|KF)&&5b8Xh^HWz1&klZ<olYN?q;$x>tpw^pjAP%F*+|uPTLDjYN62vZ}bKY<s|RQ7agZGr%ZWE=h}KL|ziz*w<y&&{6&}w+2ZaWe*zJhM373l9F=C&y6-PB!#7^{wi49x4yQt@}pqnXOg_bi0!Lw!KISiUV`-i7HpGjhpC(M9d0i&#VskBJ3GskO!kSe%<RziO0>Q76qTGU{>?|iBJGNZP-27<qpV$f93Qd+@<iQR_IWT3A30wJL*<Jk-Dq!$*NM)`eXrZZc4^ri+XoCYzuWecQ{KjRZ*$f)R>SQrwJ_i9ZAaa?B@_{=%uuZ+sIoi^P^HxXRhAQ=OT2hf9}cT99cu|H*%UAwLlr>9HZ&Sm4N)C~aZNdzFjU4UH?O1`qhj-1v3Xwkxv+QuU)fBEic1QuZOI5#lG(VvPlX9TWxQHGekyY)n9aUQe2VroNzX=xjhKm0X+2bM;uV}|TcxN{OHrwxf}tV-EStz-Gl*)%0U2oDHV0A7_4^~S`wc_IZks|psE7_5AymrCP-zz{F;rm{LZv*Giy&08gB@4Kh%y^TU<H_+S{&B1Q;WkAJM{o`KfWZ(pNgu4r+!fbPvLvOpq(PZW`0zhC|($$*C|xg_<{yJ@yMx;6_u)y+}xtyw-0#KXW^n?D0xAu@%hwz{KcYF7+&LZqjIPyRU0a5X?z})=pW8LAzzEh162sz1V=fE@F7_+6y5{>b-EHy%wkoTCIXS>!K!^>n{N#1N0uJ4Y9BLE3`BXbDg?nwR6b<XqoWhdRjDRi6<@%+kf>3*pK}!&rfU3t>7!({Qm7@WmJ{wcC^(y?9;f<eHQH*lDCo8nywtW+R17(CQSI@C0UHRTtaz2mgGL;mMF=V#Eovp8DZCH@|8;+8#MR=P;<%Y3MUBt5ln<fe3su3Q0NxHs67#sD^l()9!Lrc_3K>P4)G?N_xUYSi{iIA)xF~rPntF73d_mn>nkvvZRUApcsCdK#3p53$SfoZeXp}vn*I+VH18CccJ0}rsMq&ma0;Nm05`)yH_t(Y!0mRP|uYTLNNpt=YA2*|ik;(!?S=ma*7XlMOibow+Owx(9Bi%`Pzz2=++c%|SNk#NL5SGMELTKYH?i6VzI0JpRmR#xR8%tY7Tfwb#Ws-_E@U~wYT7&03-!o9AAd%Nif=UT-rCEO<SK}{JwO!1WXa;;Y`vPG}WW;rq%Ums@984cf<(4w#@Du)M<m!GA3+_$mzu4T>jJg^zb){Bz_2MFTrM%o#l>acA7F5NcQkfd7j4Kr>9ad_5UVbm_z*ml1%n+=6qKPjxa>7gDo5oIDsrzX*OK{UtXeqV~au}8qREj1!{T`q;u#{rCJ^Kr4#zvv+=#!iLiW-*fETm8ZNts*r5jCn|g-3LpO63A$Aqp8@vDD)XeVWW}HC#1|#l2$Qut*w8a5Yz6RfU%_3Q`2Q7t7)f#zT&}X*B4HAm73_){fHZW!UzHnL3JI5#Ma^L~K3)=nXW*(vWr<n|x@^DBo~o6z}X1Q>r$^l&TLg6=Sa9lgdaO>2OxnNS0zE3$Jk`KI0iNrbtzDkf|lrB+AqZ7kmOEDOkV{ZIbbYt;Lw?+vrbmWP(f)k)^7LtbH2WAk9A<bn)YpW>Kcxie`nGQgvab=5@6dXcmD>(abPYJeM%(Vt3_IrnAr|0%!f$FjEp`$||=yI*WF;)UNS+yB5RIQ>8Xmaas~(ir@aM&$1!-h&IxyNv#Vs_ZH>B4XH&&e)e&;{bW8RE~-T-qCIB7TC$4TBB~`fWih6<3To+|r}YB7tZY;mQ0unHikwPTD^oN&yj0W>)}jR<R#nvUBnvV{wdU4g%{VP%(ZR1o8>_13n{CII2hKvd8q(q@#ag9$87(m@7VwlRk~L=LGn)ly@yfqxh^fXArbbE@lZqBWWi-qFAWri5LQN&LgqE}#D@xk>OlA{W55l!XO~M_d)vM5~II1DD8i84~BBvIUJZKPFin2EkD@6<Ut$n{uZzuAjn}`ysj>*E@L(_S{IzgpW3CbE@WGWVB&@diVebmi#I*Q@^)lAl07qgcvMjPp`CZLo%q>2HhVxA2R0!r}+Z2)DNtZnuyQsuPqaG^S^l+M7?gWKwhEM+rceZ)=neG4ugc5-%DC5ELtd8kddCiGSPEd}a|20J^8O8INQ5XasVvR7bTvgDctUH!AQq!l|Md@F$2@Kqobm52!CYSP&NR_<QfprUzi#8fjBD_|B&+Rn;;Hi#8S#HpOn^m15O>@k6*HCE*(<aiN?giegum1$MXDLXkw%j^d$Kv)Tm?fh;YY>NCVTZlH5t%n+hoATUHA8(2hvxrl=b21p~py{KTG#1oDsxlhuU`U>`a=<Bm>6XOW#|tY?b3v>`<v6VI$$(aBsRW6xj5u{9q$suAdM|}Vec#oEn~+mIvI{UkY%@G47D?V-&SUM#uxLHl`4ChiS`2hEC!sG06?<!E09ler6Io)rRS{WU?{GDcm9uetKvr!Ks^YZtp;&o)#E)X-ZIB#;#p^8>!Kx&%^7e(7zp^&PR@ke&g;4$;T|t!>u&c8AE(Dx%)u2_=RRO0Q)$EHn<yFUi>?*J2Dru{#Y?iVrDL@ZiW%sK*n_6{&r}UnIy#)V&swS*lClm$}d{|woqbdfKTqUA_wAmA|AFDwtT6R^HyfxBlKST)sX#O^hS#hEC$%JLH-S(2ZX{gs>2D8G=aK%?pR^w+OX<KG*>_i-GQ%tJdW`cR76|XIl?M1nc!R<n=O3krWO5&I}<Pj(uEjxKQhU_9lW38Q`?UU_{TczwEa@O>r<*&%}?e)lyxtDsiJ%WdR#cksr$9GKIF5##{FGo9P!{nA>SXdVJsp+Iy(F*L}VCzRqJUB9?zem#FwBzKqvt3$a<4JOlYy5574rI-EjG=gijjAiY6)B+j8tmg0Nh~r|s~M~#EHWgq0=}Xw?b{&Ay3x&qt@4_Q)znpRpRp9FQgn8^j=Z7?gj7ODs>myt)Re$kW{0mz9UG$tyy96bHn|_Yf_0nXd1ixG^pPO3C7HT{)aV#<wuD`=#bSI^-jG$=T`-yjT=A@DU}6SowNHZ<ITpgsF++;Xz^sI$(&CvE52R3bwk6am%SX74a8}E-4`eVaRr{emQS4+IIK+d_T0pIG;i_mG8dS~D^Yy*_xA(^9Js;nrDZmT6GH)ebQjJ?_D5%I=$!pKqF@jt14t51>MTqs#Bto_ba7FLG4!Gj(%L7;Y6@0e*Mbt{%>Yi%c>Nn7B*ILJMvZDGwg0?!SFm2kPneSIi<Fj27&xlhR7*XxsMNbzzjCQ2M(Q)JO^+c>P`^M(8d~iC$9P)5h^zoX$7q#M)<LQDXuGH}oV}(*#?_whbuLM8&cFC$k<FBZ({X)bl*hnpS?^M)hRo(Z%ReX+nL9(S~xN08bJRB`7s3%ot#J{r3D68>ni;I0poCR6wKJV(wg*r7~H8&c+3&|i^UC!zutaF`oKWue?elHm<E+&$u>M5&7R38>;q|C)i#!BAhXn~|<@arBxwIzAvZA7j1!`(?gDMCd7hA0d(Y?}1!{u2+^{lih~IBmWz?AFJ9?30r6#)##rFxIFZ+Hj$zP>&3V&iER(mmyk%W7t-3AuBppKE!ISFXdALt!XH9R=<j{l2MMiOy=A8D~u0S^(j8=R4t6CEacP=bL-<&J&xWbQE*SNAD*LKd*BDax&i_Zvj&ex9lfZiGChFpC3HGEnmY~eaVhLl_6RK^v_>lHh2wYWE296nFYsYeb01kNcmn9UCGzRW?$cfgNMi>X{zp88@wG+laz1RHcYJmURgACU_0Th;BeC${H?>H+o}J@J2+&_c&}0kfHLL(o<8czk$J6HQl+-tVYeCUO>*GUz)FLWY-^_9?cn~AEyVxC{)l#kjKlM26nUhLfL~$<iwCh36@l(-LG!l%+5AbNL${-xDK+|O%(Pgp3%qD7r8s~qy*j03ka&LJUQw+5=g{b%)3`16Wy@>U+%TeVqs^5$-?8jdX9fnGap&UY`l~&(FPw{!TBMem`XqBVlOyDXfNtmfQaa@|%RYsX-;M8M0qPpX2;yf+FQ=HX+Q(DhSLj|8YKyp&mu~T9<Ec6&v?>I(D5uVc0L-LO>ioZ%kiEM?Pk|}!_QbpY|Y$`E>m7EPEL4t!_`uHdf`2)ihH6o+H8S^}sEi83E<iz+aL<KVK<udf<Hx|FqLh4kA>}7N+lTK|dsJ-Bn?%WP3O6g(`HuWfmww4|xbZV~e4wDi+#nKP$NaUmEC31>~J=c4n2{kpBlSF*;0yYUU#hS;a=#Q?;7>{{!ivAQb_~0o@+cggle%NUzN)|U|bc$1s&xm40=})Q%<1nH06^>|C156!M3(z8<;84!PqX9(!f?R5jOpU+lr)0HICUouX?GeHikf6eN>$j_*DHdpyc%12}nY>iKmRekjr(q2)Wvi~>rS=cQrL;pDb6Ckt8BR%5vj~g=EXBRCCt$Os2uqQPy9-Bkq?A!xVJ5_CDJhdkT|dk{WRZ|MNVXCt{|Z?hHa(9??T2Lovr9RYl&k@Kgw%uaQWqjxgsypD14-dI`dKuqM@5cXMC#WRLUcAD#g~rTg-J6&D!YOX`OU6*yQpc%Nac)&@ino6&@U<foT4AxACBm$s|YD<A|A)Qbal!sIEpM?DB_TM8gH+=z#A`i`LsaxA|_V@I;v>2!PUZ64WwNqAf?y2IP<|#T9!*fiHmxm%f?BckSGU;3hP5w(L7*zK||c8`*|o%Q!vUDE3Fw+lv&k^<|z?T2QkoB!liDJgu<|28fv9dNklyi+X_<D*YHXr%Gy9M%$6!XxW^L14@B{#YD7fs&srsm=vhpZEckO->!2vR&K8@hfJRl4QIZNZxLC(SNy?KHcyqWEcTFuh7V6=6u!xhxBQ2nPC=}(%cXXM7vS#H%yfkzNRDpns`WV_t6#+FjO7fTe2oywa*h>qe(ZfF>sgNnhJ4suVm|Ho@Nw-5^DzZ%lJIPBnJu*rcSh&>#O^;A4822rD87AZ+zhjuL)Ur$Saugib*Nl}ki(GmLa$&((u;N%DQA*E`X=3g0CXu5=t2uMIVdN+*;41H`i5q2`X$4us*ikuw=8qa>eWpJTM3GbgOM3A&!m!;FJc!9(CYCTcy0k$N=2l~tRx)!333eVf4jhHLZ{quSuw=LPfjswy8N^be&6+{3b24U0_t7k3=_oD3l8jiw&$N#xIbi7^kZW2jbyJsFI!NB6MM<>K(n0d+mA{ck3yIV+OW5{VN{$PJu9>9=uv+Tyt1lr-TqMo4NId--Su*cBB{z;L5lep8Z+5-l0d`>}asvd$ds%>#fVd1&Z7r1Gq({hWr7u=NNqJAIpGGR!7bO;{U{iRAq~f$I(nw`nz)vIP^?ybq>D7#}q>b_Hr;&=f-OD3o`n(a4<S6D6hGf-ffj=s$PM1Cs73I=LS~dCbBUddJ*(0k8%dC-ARb|A;sHZYjl&K^SO=LE3y4hY$6+~pb`x!w*Q?e2vdIWo7XgD_d6+2~8KRd+P;G7-thdy+HK5!^24|@l^Ai#3uW~d>_9rm&G?U4Fp+W|Km3dz*$^X8P*v1uhLMC%L;R5r;M)l#=Zi%a$^ZtsWe*nysDQ(5$z?G*8U;W08Jp}&1$nH<wYgyk+?2p24bo!Qcbt{xIIuh78lL4)?gy~pFGxQIpi!x$K<&ydhw-Kag8AC#(P`8w>&eu8}lEy?<~fC{2@IIoQ$4-yRQ<Lt_WC9<+WdrJ3f`#tO#BdLRP&^pD{rD?J}3742X-u4nf^a#56CreLKegK+^dy6fUW<xCco~g(K;bd245c;X0hbaO3+BRDS8uYkA3Lpk2=gofBE^n08MP*vSC*#mV);cT0L0HU>782l5O1^A|y(BLjWb7M`%Y;mIc#!UYoluDeS^Jk}vRJ@=K#2SaIK+x|79)f!yR_|=n9{r2fXpL8+D+3J---ti;uO4nb`~i=9i*LM_-*_snE?lxF=@O|85}SJ2|7Su#$ng8R(;qC%=!8o0YNl%oZILF@;nN8Lxc8#vyJnka!(Z+G<Td5`hi!2^B~h?&{2X}c+(>4WO&fy#x22F9YAP)09XBzO9;seYxq&SIn4#px`=!$&NiLFgUnW)e&>b@O1xCieiR#706=UBqJo|X>#3k8!V(p<@%o1wZ+&w8;yZO*(7n}M&}9AMWbNC@`ub%3nIC}#O;#^WR^OPce>=T=b^7Lc98A{UpRAvptiL{4`+l;1jc%N*|8cT@VX}S(by2;jbnVmY=PzA9|4b1La<X2N0&<KH6}$e)Wc`)N`iFAOqCy*gxiVROar*mjCabS|Ss}jn(q!$*WbGX4M_Ycla`O5|=Ss*BXUuwMvi9;1-@iS*^oC0gO`m=4#+zsJ+|cyY`5(S}1=+8kIlp=K8xJ*f{o5-WuU(zK^v8|YF5P(h{W3Tt-Ff|Q*CwmqPoIDFhwt9Xu|qdrdmhht<M*c<z(Z2h^z+X*o<B1^dycY{tJe(CWc4}8?(##EwN;zwhleJs&r>^JdS<fv^!0NeY`pVQJw7x&^~vVB&!#UvH~rhw(hz<R7kS9wrGGJ5yIP49-8ucsJJ-K`f3mtZS$%i1h6Z2ev2<;+{_OUGMU&M}(HHWVbiDrRWbFepO242HvU*;R8F~a7w3F43Cu>OmV6ytr=BuAgRxfgk|2A2Db8>QR<E@jMe_gw=et!B2y7=<+*%y(2<GnK*mp(9se1>5(eetvDGhbskqmaq!>B;JQlhs$L4JX$e1WAhVF-T^zT;nEQxp8v!hwsl+F-Y$8;U~o7easUX^YCRJc&96vq>Vp(xcSwef4FjqUrDYXZY`Vi_iKNiez1Da^pEE!c-AY={cz=Z4D;zrPv0~B{4A1WI8%o`^E<rA>#yN;K24Wa&p{eZFaMeQTE8UodOn?=TE~NJUb#H|44rfC#;F%Kzq?FtV(kT+`4+=U)64JPIRDD#pP$~i@b2~X@9^B4pPku!^~324ukj<iJN@qc&F8*CYw^^`y!q?}dN=uTyz$n>jk9lEKYxv~@l#Ac{oRe%p4~Wk4r2WJ$(N>Yos;7mAH0jM*!<J^8z=vS8zBw(F6pbkOx9kJ9%x1`iJ-vSp^^W>sm;Hh!8@YktN*!i<yo33EWaC&N?8)!{{35<m;OYv=5MED-tkjr@8_qXmI?}p<~d1(7bk0HC+ojsx$qk2xxjPyEX{<~7pC8zy8h9s?dPn>>F-X_kfPc3w0D-@1khwf2u+7)eh<O3@d?U&(Uvhi`F!Q=MY>7LWs(E$ZT{)qjb~nR_$C=;dBW+3Z=rMEk#XrzP9n>4kW)d;dRV8)I`qQtNe-<+u!zXLC{o42o~&}#DfV1|C+hOmtLWT}dJ<bDL!KsUm$-N|<Mll9R4`^7^l7sG77NH{GW6;C?=P}oxjb2ej=EgMK$*FDe){Q^jW1rU#GkZjwR#>iX1acQ`prjMM4vG6H?Dj#J$d%lfKOJ=Xj5?QWvX2Z)#A{Wu_V)H<Jsq7>ukRN&Gm~fmM6<(^%W{pciN{`^w|t00xB=(&O;@538;;?&uoxtKJNjaV8MxjlxLnq)A?|x$=cVfXg}Wg=4~JDWOO;Y<vbZZYgZ@hZ;NW4K|bZATwbMr43$1vd)`YwQTJym{Y@_bRnAkzKvAp7+7YARS$<l~%1^yG6bV9-e_ybn|9uS;HCca0+t{lYH{bkjliySo5H(qULmP@LR&P9a>c-nI<KN~$)W2+g{byvrfcX2hXJCfjIC*;GjX(VT+OriT)MQQU%a{1y)7mi8ZGL?w8I@I63q^?-sG*{~&8Q%xChMPa_nhUtubRQ~UL`Ii6AOmG#=GB^Nh!3Qp5U8Ti<p!)<^T3{FoTsUC`|pZb+nY3>X)mYy9iBf{NX%_nUYzq*GUdK^~05Cub+Dv6*%nF^z3WX)h~VQ)aHe6Hokm^BnUshp{8K2TV@JojEhXc;G7LiP2XAD{L7cJ1Zzf1ZG86S^y(MCv8%R*kW|T5dEv&%_o#P2eR}$r|D<*5SFk>waZRNvV2XO}n~(IGZS}INk!FEYlhwb{f^GE$ceN-@K-Y^DZ$M3n8u;NmF}}|kYw`6$>kHgedCgCz{Q1i_&b;FTsq~uJm^FEhiZwp`7a!Xdm-hNiUwTo-L?ui${Udt+3z{u;7?oX~PuBm$B4%|4NoChFH(rHmd9}<^iHa+dRC1eCRY_98xddm1+vG}sO6&X8%QrrL!)->6pdv})2dFT+8sSrzG&O#MnJ`t>yVdvB(N*Gp$bnUC@ry2Bg#lSfSQYZ2r#8O+-0i6{ZdJZz^D5R8&t3l>E3nt~OLf_+8}D7hK)~r_{W)t;`v5G-Sbke&49l9hRQrW5-La4dv8Ja!oSy!mio=3&k-O^0u;4tyD6RvrHb4GUH#|SuT?|WF0(mZ(izt>f#l2j_u?lva7stY->D5#9EEe*VU$d9TlANsTUbTy%S~QDC1zSODSGC^)9-7q)SfDomwDhWg^)T);X16Tn$#>8U&!WX8H0R%*ZUki^_w~=dF6OR;v8Zrvrj>+^P%PY55Q$zIOXL+!MKx8RSni^bY@pL0$cQQ6Sd;a?u#4=ff2nA>EIXN~UT2CnVY9S5oRyC}U}H+lE|;1RTII}jbQTtA@{%l|Rai%BM9cQvEJ$m5`iqRvntuIJj?W@BPJQr6)^i5Z+Pw0S%vMWiZF~zU59{Fh9Hliq`)Als&}tUanx47@%O)eVuD|`27>6Z5%a%wEDq7!M<DH6Y8LO2I1Z}XsR^qkFZg%II<860AE$hA@!DkGQ0<iVNm2Vv{Z~@qwKKrS?=m)k6o@eq8`I#+i#*}ESvgzUhw#sv}h-_J-!%u1z42=xck|ma1w6MAE=d|jL2rso&V>mRzxT>^&iRmh6<^tJO*2WIoC3??AyF}Ib$S%>eMW(BuUCU&bXuUGl<!ZVz+U3=59?Gk{=Vo`<s%Wp`mJ4oq>4lBA-gR}ExQD#-7Yo&O*7qNh9%P3UHZlAVSRwZYE#N*Y*W|;(ino6A+H~zrThZ3YFzrz`t|N%xjnCIe`}5vTp*`0xV!nMZn~CD@H_ATqocX{pn7QOwTK#x>_VbNbUoSu9PmPXQy+a!r{2pXWtlCt`xf8bwAIq!|*;8S2hqgx8lA*0`BkX98gs07nR&EbNmK$K0!0)YXu3cr<<_qvo+<5aP?^2((xTMW^BD0>Sz3wZ}aWBKINXibwz&<19*ZVMTp7uW4c7tYmWBjwPSx9{h0VrJ!XFm_;7u~%mtEZ^VXXWZ?dSvrZ&==GvwEuV7`#9Uko5_=4n*_}=LU-2l<eHm3hTL9yPS5ic0W@s_`{A?cXQ!v{Jg>7<fM*~RHa@(B6^G8YHR{Y~XjT(vG!IWbW95ODINSKcI<y70ohb3YfA_MVH?uYxB~q?B;LLqdMX05UK0AD`qo&Whc7Ey8fOp<CS^tB!66?@27{Yq+zx|cF>69nW%8o90rMwIpFIB$hoEKR&f6LYhga@{Izwjez;(6rlIE`D>QE6u5>ay$cv(C#IWSZF+B8e-zFf=``T)uJgB>NE8EJ)FmQZuDo7Vre6Y(9Nv`rK9Pdh{b{KYaH+hPRh$AeS(k8X1?ykif?q&wMLIYA%hW<=S(wIVIHr)2^RCDeRWv(#)dbojjVxyA8iHX6MHxLXGwupMTZ*rt)lB!KjiEA%vP(WL`*(EwwXjX?&dDA<EkUzy0lR|1U~7T<!')))  # Replaced with compressed JSON by the standalone builder.
_PACK_CODE = re.compile(r"^[a-z]{2,8}(?:-[a-z0-9]{1,8})*$")
_PACK_PLACEHOLDER = re.compile(r"\{[A-Za-z_]\w*\}")
_PACK_HTML_TAG = re.compile(r"<\s*/?\s*[A-Za-z][^>]*>")
_PACK_MAX_BYTES = 2 * 1024 * 1024


def canonical_language_code(value: object) -> str:
    """BCP-47-style matching, accepting the host's underscore and encoding suffix."""
    return str(value or "").strip().lower().replace("_", "-").split(".", 1)[0].split("@", 1)[0]


def validate_language_pack(raw: object, filename: str = "catalog.json") -> dict:
    if not isinstance(raw, dict) or type(raw.get("schema_version")) is not int or raw["schema_version"] != 1:
        raise ValueError("Language pack requires schema_version 1: " + filename)
    if not isinstance(raw.get("code"), str):
        raise ValueError("Language code must be text: " + filename)
    code = canonical_language_code(raw["code"])
    if not _PACK_CODE.fullmatch(code):
        raise ValueError("Invalid language code: " + filename)
    name = raw.get("native_name")
    if (not isinstance(name, str) or not 1 <= len(name.strip()) <= 80
            or _PACK_HTML_TAG.search(name) or any(ord(char) < 32 for char in name)):
        raise ValueError("Invalid native language name: " + filename)
    direction = raw.get("direction", "ltr")
    if direction not in ("ltr", "rtl"):
        raise ValueError("Invalid text direction: " + filename)
    order = raw.get("order", 1000)
    if not isinstance(order, int) or isinstance(order, bool):
        raise ValueError("Invalid language order: " + filename)
    translations = raw.get("translations", {})
    if not isinstance(translations, dict):
        raise ValueError("Translations must be an object: " + filename)
    checked = {}
    for english, translated in translations.items():
        if not isinstance(english, str) or not english.strip() or not isinstance(translated, str) or not translated.strip():
            raise ValueError("Translations must contain nonempty text: " + filename)
        if _PACK_HTML_TAG.search(translated):
            raise ValueError("Translations are plain text, not HTML: " + filename)
        if sorted(_PACK_PLACEHOLDER.findall(english)) != sorted(_PACK_PLACEHOLDER.findall(translated)):
            raise ValueError("Translation placeholders differ: " + filename)
        checked[english] = translated
    return {"schema_version": 1, "code": code, "native_name": name.strip(),
            "direction": direction, "order": order, "translations": checked}


def _language_json_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON object key: " + str(key))
        result[key] = value
    return result


def read_language_pack_files(folder: Path, strict: bool = False) -> tuple[dict, list[str]]:
    """Read only immediate JSON files; invalid optional packs cannot disable the UI."""
    found, errors = {}, []
    if not folder.is_dir():
        return found, errors
    for path in sorted(folder.glob("*.json")):
        try:
            path.resolve().relative_to(folder.resolve())
            if path.stat().st_size > _PACK_MAX_BYTES:
                raise ValueError("Language pack exceeds size limit: " + path.name)
            raw = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_language_json_object)
            pack = validate_language_pack(raw, path.name)
            if pack["code"] in found:
                raise ValueError("Duplicate language code: " + path.name)
            found[pack["code"]] = pack
        except (OSError, ValueError, TypeError, UnicodeError) as exc:
            if strict:
                raise ValueError("Invalid language pack " + path.name + ": " + str(exc)) from exc
            errors.append(path.name + ": " + type(exc).__name__)
    return found, errors


def load_language_packs(folder: str | Path | None = None, *, embedded: dict | None = None,
                        strict: bool = False) -> tuple[dict, tuple[str, ...]]:
    """Bundle data first, then optional local JSON overrides, sorted by metadata."""
    packs, errors = {}, []
    for filename, raw in (embedded if embedded is not None else _BUNDLED_LANGUAGE_PACKS).items():
        try:
            pack = validate_language_pack(raw, str(filename))
            if pack["code"] in packs:
                raise ValueError("Duplicate embedded language code: " + str(filename))
            packs[pack["code"]] = pack
        except (ValueError, TypeError) as exc:
            if strict:
                raise
            errors.append(str(filename) + ": " + type(exc).__name__)
    directory = Path(folder) if folder is not None else Path(__file__).resolve().parent / "locales"
    files, issues = read_language_pack_files(directory, strict=strict)
    errors.extend(issues)
    for code, pack in files.items():
        if code in packs:
            pack = {**pack, "translations": {**packs[code]["translations"], **pack["translations"]}}
        packs[code] = pack
    packs.setdefault("en", {"schema_version": 1, "code": "en", "native_name": "English",
                            "direction": "ltr", "order": 1, "translations": {}})
    return dict(sorted(packs.items(), key=lambda item: (item[1]["order"], item[0]))), tuple(errors)


def resolve_language(value: object, available: object, default: str = "pt") -> str:
    code = canonical_language_code(value)
    if not code:
        return default if default in available else "en"
    candidate = code
    while candidate:
        if candidate in available:
            return candidate
        candidate = candidate.rsplit("-", 1)[0] if "-" in candidate else ""
    return "en"


def language_pack_payload(packs: dict) -> list[dict]:
    """Metadata is used by the UI directly; there is no second locale allowlist."""
    return [{"code": code, "native_name": pack["native_name"], "direction": pack["direction"]}
            for code, pack in packs.items()]

# ===========================================================================
# MODULE: thread_studio.locale_catalog
# ===========================================================================

"""Thread translation adapter. Catalog content and available languages are JSON data."""
pass  # [bundled] hoisted __future__ import

pass  # [bundled] resolved intra-package import

LANGUAGE_PACKS, LANGUAGE_PACK_ERRORS = load_language_packs()
SUPPORTED_LANGUAGES = tuple(LANGUAGE_PACKS)
LANGUAGE_NAMES = tuple(pack["native_name"] for pack in LANGUAGE_PACKS.values())
LANGUAGE_METADATA = language_pack_payload(LANGUAGE_PACKS)
TRANSLATIONS = {code: pack["translations"] for code, pack in LANGUAGE_PACKS.items()}


def normalize_language(value: object, default: str = "pt") -> str:
    return resolve_language(value, LANGUAGE_PACKS, default)


def translate_text(english: str, language: object, portuguese: str | None = None,
                   context: str | None = None) -> str:
    code = normalize_language(language)
    catalog = TRANSLATIONS.get(code, {})
    if context and context + "::" + english in catalog:
        return catalog[context + "::" + english]
    return catalog.get(english,
        portuguese if code == "pt" and portuguese is not None else english)

# ===========================================================================
# MODULE: thread_studio.schema
# ===========================================================================

"""Validated offline Thread Studio parameters. Dimensions are millimetres."""

pass  # [bundled] hoisted __future__ import
import math
from dataclasses import dataclass, asdict
from typing import Any

pass  # [bundled] resolved intra-package import

SCHEMA_VERSION = 1


@dataclass
class ThreadSpec:
    nominal_dia: float = 40.0
    pitch: float = 3.0
    thread_length: float = 12.0
    starts: int = 1
    hand: str = "right"


DEFAULT_PARAMS = dict(
    asdict(ThreadSpec()),
    module="container_and_lid",
    standard="fdm_trapezoid_45",
    part="cap",
    name="Orca Thread",
    diameter=44.0,
    height=55.0,
    wall_thickness=2.4,
    floor_thickness=2.4,
    diametral_clearance=0.26,
    axial_clearance=0.15,
    higbee_turns=0.65,
    knurl_depth=0.5,
    knurl_count=40,
    texture="knurled",
    head="hex",
    head_height=5.0,
    bore_diameter=0.0,
    inlet_diameter=35.0,
    outlet_diameter=58.0,
    adapter_length=65.0,
    end_length=15.0,
    end_a="smooth",
    end_b="barb",
    gasket=True,
    gasket_depth=0.6,
    gasket_width=1.1,
    gasket_offset=1.1,
    auto_configure_slicer=True,
    export_target="all",
    measurements_confirmed=False,
    measured_major_dia=0.0,
    measured_root_dia=0.0,
    measured_pitch=0.0,
    measured_length=0.0,
    lang="pt",
    theme="dark",
    resolution=96,
)
ISO_COARSE = {
    6: 1.0,
    8: 1.25,
    10: 1.5,
    12: 1.75,
    16: 2.0,
    20: 2.5,
    24: 3.0,
    30: 3.5,
    36: 4.0,
    42: 4.5,
    48: 5.0,
    64: 6.0,
    80: 6.0,
    100: 6.0,
}


def _number(value, default, low, high):
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError):
        value = default
    return min(high, max(low, value)) if math.isfinite(value) else default


def normalize_params(raw: dict[str, Any] | None = None) -> dict[str, Any]:
    p = dict(DEFAULT_PARAMS)
    if isinstance(raw, dict):
        p.update({k: v for k, v in raw.items() if k in p})
    p["lang"] = normalize_language(p["lang"])
    choices = {
        "module": [
            "container_and_lid",
            "standard_bottle_cap",
            "hose_vacuum_adapter",
            "bolt_nut_knob",
        ],
        "standard": [
            "iso_metric",
            "fdm_trapezozoid_45",
            "fdm_trapezoid_45",
            "pco1881",
            "mason_70",
            "mason_86",
        ],
        "hand": ["right", "left"],
        "texture": ["smooth", "knurled", "fluted", "faceted"],
        "head": ["hex", "knurled", "wing"],
        "end_a": ["smooth", "barb", "male", "female"],
        "end_b": ["smooth", "barb", "male", "female"],
        "part": ["cap", "neck"],
        "export_target": ["all", "primary", "secondary", "calibration"],
        "theme": ["dark", "light"],
    }
    for k, opts in choices.items():
        if p[k] not in opts:
            p[k] = DEFAULT_PARAMS[k]
    limits = {
        "nominal_dia": (6, 100),
        "pitch": (0.5, 10),
        "thread_length": (3, 100),
        "height": (12, 200),
        "diameter": (12, 150),
        "wall_thickness": (1.2, 8),
        "floor_thickness": (1.2, 8),
        "diametral_clearance": (0.05, 0.6),
        "axial_clearance": (0, 0.6),
        "higbee_turns": (0.1, 1),
        "knurl_depth": (0, 1.5),
        "knurl_count": (12, 100),
        "head_height": (3, 15),
        "bore_diameter": (0, 90),
        "inlet_diameter": (10, 100),
        "outlet_diameter": (10, 120),
        "adapter_length": (30, 180),
        "end_length": (7, 35),
        "gasket_depth": (0.2, 1.2),
        "gasket_width": (0.6, 2),
        "gasket_offset": (0.6, 3),
        "resolution": (48, 192),
        "measured_major_dia": (0, 120),
        "measured_root_dia": (0, 120),
        "measured_pitch": (0, 10),
        "measured_length": (0, 40),
    }
    for k, (lo, hi) in limits.items():
        p[k] = _number(p[k], DEFAULT_PARAMS[k], lo, hi)
    p["starts"] = int(_number(p["starts"], 1, 1, 3))
    p["resolution"] = int(p["resolution"])
    p["knurl_count"] = int(p["knurl_count"])
    for k in ["gasket", "auto_configure_slicer", "measurements_confirmed"]:
        p[k] = p[k] is True or p[k] == 1
    p["name"] = str(p["name"])[:80]
    p["standard"] = (
        "fdm_trapezoid_45" if p["standard"] == "fdm_trapezozoid_45" else p["standard"]
    )
    p["height"] = max(p["height"], p["floor_thickness"] + p["thread_length"] + 4)
    p["axial_clearance"] = min(p["axial_clearance"], p["pitch"] * 0.2)
    p["end_length"] = min(p["end_length"], p["adapter_length"] * 0.28)
    p["gasket_depth"] = min(p["gasket_depth"], p["floor_thickness"] * 0.45)
    if p["module"] == "standard_bottle_cap":
        if p["standard"] == "pco1881":
            p.update(nominal_dia=27.4, pitch=2.7, thread_length=7.0, starts=1)
        elif p["standard"] == "mason_70":
            p.update(nominal_dia=70.0, pitch=6.35, thread_length=7.9375, starts=1)
        elif p["standard"] == "mason_86" and p["measurements_confirmed"]:
            if not (
                p["measured_major_dia"] > p["measured_root_dia"] > 0
                and p["measured_pitch"] >= 0.5
                and p["measured_length"] >= 3
            ):
                raise ValueError(
                    "Mason 86: confirm measured major diameter, root diameter, pitch and length"
                )
            p.update(
                nominal_dia=p["measured_major_dia"],
                pitch=p["measured_pitch"],
                thread_length=p["measured_length"],
            )
    p["lead"] = p["pitch"] * p["starts"]
    p["bore_diameter"] = min(
        p["bore_diameter"],
        max(0, p["nominal_dia"] - 2 * p["wall_thickness"] - 1.3 * p["pitch"]),
    )
    return p

# ===========================================================================
# MODULE: thread_studio.thread_math
# ===========================================================================

"""Analytic radial helical envelopes, ISO-inspired/FDM profiles and Higbee starts."""

pass  # [bundled] hoisted __future__ import

try:
    import numpy as np
except ModuleNotFoundError:
    import sys, os
    from pathlib import Path

    base = (
        Path(os.environ.get("APPDATA", "")) / "OrcaSlicer"
        if sys.platform == "win32"
        else Path.home()
        / (
            ".config/OrcaSlicer"
            if sys.platform != "darwin"
            else "Library/Application Support/OrcaSlicer"
        )
    )
    sys.path.insert(
        0,
        str(
            base
            / "python/packages"
            / f"cp{sys.version_info.major}{sys.version_info.minor}"
        ),
    )
    import numpy as np

pass  # [bundled] resolved intra-package import


def thread_depth(params):
    p = normalize_params(params)
    if p["standard"] == "pco1881":
        return (27.40 - 24.20) / 2
    if p["standard"] == "mason_86" and p["measurements_confirmed"]:
        return 0.5 * (p["measured_major_dia"] - p["measured_root_dia"])
    return min(
        p["nominal_dia"] * 0.12,
        p["pitch"] * (0.61343 if p["standard"] == "iso_metric" else 0.375),
    )


def higbee_envelope(z, length, ramp):
    u = np.clip(
        np.minimum(np.asarray(z), length - np.asarray(z)) / max(ramp, 1e-6), 0, 1
    )
    return u * u * (3 - 2 * u)


def thread_profile(phase, standard="iso_metric", axial_widening=0.0):
    # Symmetric truncated 60 degree / 45 degree radial tooth.
    signed = (np.asarray(phase) + 0.5) % 1.0 - 0.5
    if standard == "pco1881":
        # ISBT-derived asymmetric experimental envelope; rounded tooling details omitted.
        q = signed
        return np.where(
            q < -0.12,
            np.clip((q + 0.31) / 0.19, 0, 1),
            np.where(q > 0.10, np.clip((0.30 - q) / 0.20, 0, 1), 1.0),
        )
    q = np.abs(signed)
    crest = 0.0625 if standard == "iso_metric" else 0.125
    root = (0.0625 + 0.61343 / np.sqrt(3)) if standard == "iso_metric" else 0.5
    q = np.maximum(0, q - axial_widening)
    return np.clip((root - q) / (root - crest), 0, 1)


def thread_radius(theta, z, params, female=False):
    p = normalize_params(params)
    z = np.asarray(z)
    theta = np.asarray(theta)
    sign = 1 if p["hand"] == "right" else -1
    phase = z / p["pitch"] - sign * p["starts"] * theta / (2 * np.pi)
    depth = thread_depth(p)
    widen = p["axial_clearance"] / p["pitch"] / 2 if female else 0
    tooth = thread_profile(phase, p["standard"], widen)
    if female and p["standard"] == "pco1881":
        tooth = np.maximum.reduce(
            [
                thread_profile(phase + shift, p["standard"])
                for shift in np.linspace(-widen, widen, 9)
            ]
        )
    envelope = higbee_envelope(z, p["thread_length"], p["lead"] * p["higbee_turns"])
    # Female groove retains the full envelope, including a major-diameter lead-in.
    radius = p["nominal_dia"] / 2 - depth + depth * tooth * (1 if female else envelope)
    return radius + (p["diametral_clearance"] / 2 if female else 0)


def analyze_engagement(params):
    p = normalize_params(params)
    theta = np.linspace(0, 2 * np.pi, 97)[:, None]
    z = np.linspace(0, p["thread_length"], 257)[None, :]
    clearance = thread_radius(theta, z, p, True) - thread_radius(theta, z, p, False)
    return {
        "lead_mm": p["lead"],
        "radial_clearance_mm": p["diametral_clearance"] / 2,
        "axial_clearance_mm": p["axial_clearance"],
        "minimum_radial_gap_mm": float(np.min(clearance)),
        "interference": bool(np.any(clearance < -1e-8)),
        "experimental": p["standard"] in ("pco1881", "mason_70", "mason_86"),
        "physical_fit_verified": False,
    }

# ===========================================================================
# MODULE: thread_studio.mesh_generator
# ===========================================================================

"""Connected watertight radial meshes. Threads are surface coordinates, never added solids."""

pass  # [bundled] hoisted __future__ import
from dataclasses import dataclass
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import sys, os
    from pathlib import Path

    base = (
        Path(os.environ.get("APPDATA", "")) / "OrcaSlicer"
        if sys.platform == "win32"
        else Path.home()
        / (
            ".config/OrcaSlicer"
            if sys.platform != "darwin"
            else "Library/Application Support/OrcaSlicer"
        )
    )
    sys.path.insert(
        0,
        str(
            base
            / "python/packages"
            / f"cp{sys.version_info.major}{sys.version_info.minor}"
        ),
    )
    import numpy as np
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import


@dataclass
class MeshData:
    vertices: np.ndarray
    triangles: np.ndarray
    face_normals: np.ndarray
    bounds_mm: dict
    volume_cm3: float


def _finish(vertices, triangles):
    v = np.asarray(vertices, dtype=np.float64)
    t = np.asarray(triangles, dtype=np.int32)
    cross = np.cross(v[t[:, 1]] - v[t[:, 0]], v[t[:, 2]] - v[t[:, 0]])
    lengths = np.linalg.norm(cross, axis=1)
    if np.any(lengths < 1e-10):
        raise ValueError("Degenerate generated surface")
    volume = float(
        np.sum(np.einsum("ij,ij->i", v[t[:, 0]], np.cross(v[t[:, 1]], v[t[:, 2]]))) / 6
    )
    if volume < 0:
        t = t[:, [0, 2, 1]]
        cross = -cross
        volume = -volume
    mn = v.min(axis=0)
    mx = v.max(axis=0)
    return MeshData(
        v.astype(np.float32),
        t,
        (cross / lengths[:, None]).astype(np.float32),
        {"min": mn.tolist(), "max": mx.tolist(), "size": (mx - mn).tolist()},
        volume / 1000,
    )


def _surface(path, n, flip_diagonal=False):
    # Ordered meridian rings/poles form a closed loop. Consecutive rings share exact indices.
    if len(path) * n > 350_000:
        raise ValueError(
            "Mesh exceeds the supported vertex budget; reduce length/resolution or increase pitch"
        )
    theta = np.arange(n) * 2 * np.pi / n
    vertices = []
    rings = []
    triangles = []
    for z, rad in path:
        rr = np.broadcast_to(np.asarray(rad, dtype=float), (n,))
        if not np.isfinite(rr).all() or np.any(rr < 0):
            raise ValueError("Surface contains an invalid radius")
        if np.max(np.abs(rr)) < 1e-9:
            rings.append([len(vertices)])
            vertices.append((0, 0, float(z)))
        else:
            ids = list(range(len(vertices), len(vertices) + n))
            rings.append(ids)
            vertices.extend(zip(rr * np.cos(theta), rr * np.sin(theta), np.full(n, z)))
    for a, b in zip(rings, rings[1:] + rings[:1]):
        if len(a) == len(b) == 1:
            continue
        for j in range(n):
            k = (j + 1) % n
            if len(a) == 1:
                triangles.append((a[0], b[j], b[k]))
            elif len(b) == 1:
                triangles.append((a[j], b[0], a[k]))
            elif flip_diagonal:
                triangles.extend(((a[j], b[j], a[k]), (a[k], b[j], b[k])))
            else:
                triangles.extend(((a[j], b[j], b[k]), (a[j], b[k], a[k])))
    return _finish(vertices, triangles)


def _levels(a, b, step):
    return np.linspace(a, b, max(2, int(np.ceil(abs(b - a) / step)) + 1))


def _texture(theta, z, r, p, kind=None):
    kind = kind or p["texture"]
    depth = min(p["knurl_depth"], p["wall_thickness"] * 0.3)
    if kind == "knurled":
        return r + depth * (
            0.5 + 0.5 * np.cos(p["knurl_count"] * theta) * np.cos(z * 2 * np.pi / 3)
        )
    if kind == "fluted":
        return r + depth * (0.5 + 0.5 * np.cos(p["knurl_count"] * theta))
    if kind == "faceted":
        return (
            r
            * np.cos(np.pi / 8)
            / np.cos((theta + np.pi / 8) % (np.pi / 4) - np.pi / 8)
        )
    return np.full(theta.shape, r)


def _head_radius(theta, r, p):
    if p["head"] == "hex":
        return (
            r
            * np.cos(np.pi / 6)
            / np.cos((theta + np.pi / 6) % (np.pi / 3) - np.pi / 6)
        )
    if p["head"] == "wing":
        return r * (1 + 0.65 * np.abs(np.cos(theta)) ** 6)
    return _texture(theta, 0, r, p, "fluted")


def _validate_standard(p):
    if (
        p["module"] == "standard_bottle_cap"
        and p["standard"] == "mason_86"
        and not p["measurements_confirmed"]
    ):
        raise ValueError(
            "Mason 86 experimental: confirm measured dimensions before generation"
        )


def _jar(p, neck=False):
    n = p["resolution"]
    theta = np.arange(n) * 2 * np.pi / n
    h = p["thread_length"] + p["floor_thickness"] + 3 if neck else p["height"]
    floor = p["floor_thickness"]
    length = p["thread_length"]
    wall = p["wall_thickness"]
    root = p["nominal_dia"] / 2 - thread_depth(p)
    inner = root - wall
    if inner <= 0.5:
        raise ValueError(
            "Container wall leaves no usable bore at thread root; increase nominal diameter or reduce wall"
        )
    outer = max(p["diameter"] / 2, p["nominal_dia"] / 2 + 1) if not neck else root
    if p["texture"] == "faceted" and not neck:
        outer = max(outer, (inner + wall) / np.cos(np.pi / 8))
    path = []
    if not neck:
        path.append((0, 0.0))
    path.append((0, outer))
    shoulder = h - length - 1
    for z in _levels(0.2, shoulder, 0.8):
        path.append((z, _texture(theta, z, outer, p) if not neck else root))
    path.append((h - length, root))
    for q in _levels(0, length, p["pitch"] / 12)[1:]:
        path.append((h - length + q, thread_radius(theta, q, p)))
    path.append((h, inner))
    for z in _levels(h, floor if not neck else 0, 1)[1:]:
        path.append((z, inner))
    if not neck:
        path.append((floor, 0.0))
    return _surface(path, n)


def _female(p, ring=False, nut=False, mark=0):
    n = p["resolution"]
    theta = np.arange(n) * 2 * np.pi / n
    length = p["thread_length"]
    floor = 0 if ring or nut else p["floor_thickness"]
    h = length + floor
    wall = p["wall_thickness"]
    outer = p["nominal_dia"] / 2 + wall + p["diametral_clearance"] / 2
    if mark:
        outer += min(0.55, wall * 0.25)
    if not nut and p["texture"] == "faceted":
        outer /= np.cos(np.pi / 8)
    if nut and p["head"] == "hex":
        outer /= np.cos(np.pi / 6) * 1.12
    path = []
    if floor:
        path.extend([(0, 0.0), (0, _texture(theta, 0, outer, p))])
    else:
        path.append(
            (0, _head_radius(theta, outer * 1.12, p) if nut else np.full(n, outer))
        )
    for z in _levels(0.2, h, 0.8):
        rr = (
            _head_radius(theta, outer * 1.12, p)
            if nut
            else _texture(theta, z, outer, p)
        )
        if mark:
            # One, two or three tangible notches in the outer rim, outside the thread bore.
            notch = np.zeros(n)
            for k in range(mark):
                notch = np.maximum(
                    notch,
                    np.clip(
                        1
                        - np.abs(
                            np.angle(
                                np.exp(1j * (theta - (k - 0.5 * (mark - 1)) * 0.23))
                            )
                        )
                        / 0.065,
                        0,
                        1,
                    ),
                )
            rr = rr - min(0.55, wall * 0.25) * notch * (z > h - 1.1)
        path.append((z, rr))
    # Inner female mirrored for printing open side up. On assembly rotate 180deg about X.
    for q in _levels(length, 0, p["pitch"] / 12):
        z = floor + q
        rr = thread_radius(-theta, length - q, p, True)
        path.append((z, rr))
    if floor:
        bore = float(np.min(thread_radius(theta, length, p, True)))
        if p["gasket"]:
            go = min(p["gasket_offset"], max(0.6, bore * 0.2))
            gw = min(p["gasket_width"], bore * 0.15)
            path.extend(
                [
                    (floor, bore - go),
                    (floor - p["gasket_depth"], bore - go),
                    (floor - p["gasket_depth"], bore - go - gw),
                    (floor, bore - go - gw),
                ]
            )
        path.append((floor, 0.0))
    return _surface(path, n, flip_diagonal=True)


def _bolt(p):
    n = p["resolution"]
    th = np.arange(n) * 2 * np.pi / n
    root = p["nominal_dia"] / 2 - thread_depth(p)
    hh = p["head_height"]
    path = []
    bore = p["bore_diameter"] / 2
    if not bore:
        path.append((0, 0.0))
    else:
        path.append((0, bore))
    head = _head_radius(th, p["nominal_dia"] * 0.85, p)
    path.extend([(0, head), (hh, head), (hh, root)])
    for q in _levels(0.001, p["thread_length"], p["pitch"] / 12):
        path.append((hh + q, thread_radius(th, q, p)))
    if bore:
        path.extend([(hh + p["thread_length"], bore), (0.001, bore)])
    else:
        path.append((hh + p["thread_length"], 0.0))
    return _surface(path, n)


def _adapter(p):
    n = p["resolution"]
    th = np.arange(n) * 2 * np.pi / n
    h = p["adapter_length"]
    el = p["end_length"]
    wall = p["wall_thickness"]
    step = min(0.6, p["pitch"] / 12)
    start_step = step if p["end_a"] in ("male", "female") else 0.5
    end_step = step if p["end_b"] in ("male", "female") else 0.5
    zs = np.unique(
        np.r_[
            _levels(0, el, start_step),
            _levels(el, h - el, 0.8),
            _levels(h - el, h, end_step),
        ]
    )
    path = []

    # Smooth/barb end diameters describe clear bore; male/female describe thread nominal.
    def radii(z):
        u = np.clip((z - el) / (h - 2 * el), 0, 1)
        diam = (1 - u) * p["inlet_diameter"] + u * p["outlet_diameter"]
        inner = np.full(n, diam / 2)
        outer = inner + wall
        which = 0 if z <= el else 1 if z >= h - el else -1
        if which >= 0:
            kind = p["end_a"] if which == 0 else p["end_b"]
            q = z if which == 0 else h - z
            local = dict(p, nominal_dia=diam, thread_length=el)
            if kind == "barb":
                outer = outer + wall * 0.42 * np.maximum(
                    0, 1 - ((q - 1) % 4) / 3
                ) * np.clip(q / 1.5, 0, 1) * np.clip((el - q) / 1.5, 0, 1)
            elif kind == "smooth":
                outer = outer + 0.35 * (1 - q / el)
            elif kind == "male":
                outer = thread_radius(th if which == 0 else -th, q, local)
                inner = np.full(n, diam / 2 - thread_depth(local) - wall)
                if np.min(inner) <= 0.5:
                    raise ValueError(
                        "Adapter wall leaves no usable bore at threaded end; reduce wall or increase end diameter"
                    )
            elif kind == "female":
                inner = thread_radius(th if which == 0 else -th, q, local, True)
                outer = np.full(n, diam / 2 + wall + p["diametral_clearance"] / 2)
        return inner, outer

    for z in zs:
        path.append((z, radii(z)[1]))
    for z in zs[::-1]:
        path.append((z, radii(z)[0]))
    return _surface(path, n)


def generate_thread_calibration_kit(params=None):
    p = normalize_params(params)
    p.update(
        thread_length=max(3, min(p["pitch"] * 1.8, 6)), gasket=False, texture="smooth"
    )
    return [
        (
            f"Ring_{i}_{gap:.2f}mm",
            _female(dict(p, diametral_clearance=gap), ring=True, mark=i),
        )
        for i, gap in enumerate((0.10, 0.18, 0.26), 1)
    ]


def generate_parts(params=None):
    p = normalize_params(params)
    _validate_standard(p)
    if p["module"] == "container_and_lid":
        return [("Container", _jar(p)), ("Lid", _female(p))]
    if p["module"] == "standard_bottle_cap":
        return (
            [("Cap", _female(p))] if p["part"] == "cap" else [("Neck", _jar(p, True))]
        )
    if p["module"] == "hose_vacuum_adapter":
        return [("Adapter", _adapter(p))]
    return [("Bolt", _bolt(p)), ("Nut", _female(p, ring=True, nut=True))]


def collect_target_meshes(params=None, target=None, lang="pt"):
    p = normalize_params(params)
    target = target or p["export_target"]
    if target == "calibration":
        return generate_thread_calibration_kit(p)
    parts = generate_parts(p)
    if target == "primary":
        return parts[:1]
    if target == "secondary":
        return parts[1:] or parts[:1]
    return parts

# ===========================================================================
# MODULE: thread_studio.exporters
# ===========================================================================

"""Binary STL and OrcaSlicer 2.5.1+ multi-object 3MF project exporters for Orca Thread Studio."""

pass  # [bundled] hoisted __future__ import

import datetime as _dt
import json
import math
import re
import struct
import uuid
import zipfile
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape as _xml_escape

import numpy as np

_STL_RECORD_DTYPE = np.dtype(
    [
        ("normal", "<f4", (3,)),
        ("v0", "<f4", (3,)),
        ("v1", "<f4", (3,)),
        ("v2", "<f4", (3,)),
        ("attr", "<u2"),
    ]
)

_CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="config" ContentType="text/xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="json" ContentType="application/json"/>
</Types>
"""

_RELS_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>
"""


def _extract_mesh_arrays(mesh: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract validated (vertices, triangles, face_normals) arrays from duck-typed MeshData."""
    vertices = np.asarray(mesh.vertices, dtype=np.float32)
    if vertices.ndim != 2 or vertices.shape[1] != 3:
        raise ValueError(f"Expected vertices shape (V, 3), got {vertices.shape!r}")
    if not np.all(np.isfinite(vertices)):
        raise ValueError("Mesh contains nonfinite coordinates")

    triangles = np.asarray(mesh.triangles, dtype=np.int32)
    if triangles.size == 0:
        triangles = np.zeros((0, 3), dtype=np.int32)
    elif triangles.ndim != 2 or triangles.shape[1] != 3:
        raise ValueError(f"Expected triangles shape (F, 3), got {triangles.shape!r}")

    if (
        len(vertices) == 0
        or len(triangles) == 0
        or np.any(triangles < 0)
        or np.any(triangles >= len(vertices))
    ):
        raise ValueError("Mesh has empty or invalid topology")
    area_vectors = np.cross(
        vertices[triangles[:, 1]] - vertices[triangles[:, 0]],
        vertices[triangles[:, 2]] - vertices[triangles[:, 0]],
    )
    if np.any(np.linalg.norm(area_vectors, axis=1) <= 1e-10):
        raise ValueError("Mesh contains degenerate faces")
    num_tris = triangles.shape[0]
    raw_normals = getattr(mesh, "face_normals", None)
    if (
        raw_normals is not None
        and np.asarray(raw_normals).shape == (num_tris, 3)
        and np.all(np.isfinite(raw_normals))
    ):
        normals = np.asarray(raw_normals, dtype=np.float32)
    elif num_tris > 0:
        tris_xyz = vertices[triangles]
        e1 = tris_xyz[:, 1, :] - tris_xyz[:, 0, :]
        e2 = tris_xyz[:, 2, :] - tris_xyz[:, 0, :]
        cross = np.cross(e1, e2)
        lengths = np.linalg.norm(cross, axis=1, keepdims=True)
        safe_lengths = np.where(lengths > 1e-12, lengths, 1.0)
        normals = (cross / safe_lengths).astype(np.float32)
        normals = np.where(
            lengths > 1e-12, normals, np.array([[0.0, 0.0, 1.0]], dtype=np.float32)
        )
    else:
        normals = np.zeros((0, 3), dtype=np.float32)

    return vertices, triangles, normals


def _mesh_xy_extents(
    mesh: Any, vertices: np.ndarray | None = None
) -> tuple[float, float]:
    """Return (width_x_mm, depth_y_mm) of a mesh from vertices or bounds_mm."""
    verts = (
        vertices
        if vertices is not None
        else np.asarray(getattr(mesh, "vertices", []), dtype=np.float32)
    )
    if verts.ndim == 2 and verts.shape[0] > 0 and verts.shape[1] >= 2:
        dx = float(np.max(verts[:, 0]) - np.min(verts[:, 0]))
        dy = float(np.max(verts[:, 1]) - np.min(verts[:, 1]))
        return max(dx, 1.0), max(dy, 1.0)
    bounds = getattr(mesh, "bounds_mm", None)
    if isinstance(bounds, dict):
        size = bounds.get("size")
        if isinstance(size, (list, tuple)) and len(size) >= 2:
            return max(float(size[0]), 1.0), max(float(size[1]), 1.0)
        bmin = bounds.get("min")
        bmax = bounds.get("max")
        if (
            isinstance(bmin, (list, tuple))
            and isinstance(bmax, (list, tuple))
            and len(bmin) >= 2
            and len(bmax) >= 2
        ):
            return max(float(bmax[0]) - float(bmin[0]), 1.0), max(
                float(bmax[1]) - float(bmin[1]), 1.0
            )
    return 10.0, 10.0


def _mesh_xy_center_offset(
    mesh: Any, vertices: np.ndarray | None = None
) -> tuple[float, float]:
    """Return the local XY bounding-box midpoint `(mid_x, mid_y)` of `mesh`."""
    verts = (
        vertices
        if vertices is not None
        else np.asarray(mesh.vertices, dtype=np.float32)
    )
    if verts.shape[0] == 0:
        return 0.0, 0.0
    mx = 0.5 * float(np.max(verts[:, 0]) + np.min(verts[:, 0]))
    my = 0.5 * float(np.max(verts[:, 1]) + np.min(verts[:, 1]))
    return mx, my


def _resolve_printable_limits(
    host_config: dict[str, Any] | None,
) -> tuple[float, float, float]:
    """Validate every supplied limit; defaults apply only to absent keys.

    Direct host values take precedence over nested printer values. Height aliases
    use max_z, bed_z, then printable_height, in that order, by key presence.
    Even a lower-priority supplied alias must be a valid positive finite limit.
    """
    if host_config is None:
        config = {}
    elif isinstance(host_config, dict):
        config = host_config
    else:
        raise ValueError("Printer configuration must be an object")
    printer = config.get("printer", {})
    if not isinstance(printer, dict):
        raise ValueError("Nested printer configuration must be an object")

    sources = (config, printer)
    height_keys = ("max_z", "bed_z", "printable_height")
    parsed = []
    for source in sources:
        values = {}
        for key in ("bed_x", "bed_y", *height_keys):
            if key not in source:
                continue
            raw = source[key]
            try:
                value = float(raw)
            except (TypeError, ValueError, OverflowError) as exc:
                raise ValueError(
                    f"Invalid printable limit {key}: expected a positive finite number"
                ) from exc
            minimum = 8.0 if key in ("bed_x", "bed_y") else 0.0
            if isinstance(raw, bool) or not math.isfinite(value) or value <= minimum:
                raise ValueError(
                    f"Invalid printable limit {key}: expected a positive finite number"
                )
            values[key] = value
        parsed.append(values)

    dimensions = []
    for key in ("bed_x", "bed_y"):
        dimensions.append(
            next((source[key] for source in parsed if key in source), 220.0)
        )
    height = next(
        (source[key] for source in parsed for key in height_keys if key in source),
        1000.0,
    )
    return dimensions[0], dimensions[1], height


def _resolve_bed_dimensions(host_config: dict[str, Any] | None) -> tuple[float, float]:
    """Return actual dimensions after validating all explicitly supplied limits."""
    bed_x, bed_y, _ = _resolve_printable_limits(host_config)
    return bed_x, bed_y


def _validate_xml_text(value: str, field: str) -> str:
    """Reject characters XML 1.0 cannot represent before creating an archive."""
    for character in value:
        code = ord(character)
        valid = (
            code in (0x09, 0x0A, 0x0D)
            or 0x20 <= code <= 0xD7FF
            or 0xE000 <= code <= 0xFFFD
            or 0x10000 <= code <= 0x10FFFF
        )
        if not valid:
            raise ValueError(
                f"{field} contains a character invalid in XML 1.0 (U+{code:04X})"
            )
    return value


def _resolve_line_width(host_config: dict[str, Any] | None) -> float:
    """Resolve active outer wall line width in mm from host_config (default 0.42 mm)."""
    if isinstance(host_config, dict):
        for direct_key in ("line_width_mm",):
            if direct_key in host_config:
                try:
                    lw = float(host_config[direct_key])
                    if 0.18 <= lw <= 2.5:
                        return lw
                except (TypeError, ValueError):
                    pass
        printer = host_config.get("printer")
        if isinstance(printer, dict) and "line_width_mm" in printer:
            try:
                lw = float(printer["line_width_mm"])
                if 0.18 <= lw <= 2.5:
                    return lw
            except (TypeError, ValueError):
                pass
        ps = host_config.get("project_settings")
        if isinstance(ps, dict):
            raw_lw = ps.get("outer_wall_line_width") or ps.get("line_width")
            if isinstance(raw_lw, (list, tuple)) and raw_lw:
                raw_lw = raw_lw[0]
            if raw_lw is not None:
                s = str(raw_lw).strip()
                if not s.endswith("%"):
                    m = re.search(r"[-+]?\d*\.?\d+", s)
                    if m:
                        try:
                            lw = float(m.group(0))
                            if 0.18 <= lw <= 2.5:
                                return lw
                        except ValueError:
                            pass
    return 0.42


def _positions_overlap(
    positions: list[tuple[float, float, float]],
    extents: list[tuple[float, float]],
    min_clearance_mm: float = 3.0,
) -> bool:
    """Return True if any two axis-aligned bounding boxes overlap on the XY build plate."""
    n = len(positions)
    for i in range(n):
        xi, yi, _ = positions[i]
        wxi, wyi = extents[i]
        for j in range(i + 1, n):
            xj, yj, _ = positions[j]
            wxj, wyj = extents[j]
            overlap_x = abs(xi - xj) < (0.5 * (wxi + wxj) + min_clearance_mm)
            overlap_y = abs(yi - yj) < (0.5 * (wyi + wyj) + min_clearance_mm)
            if overlap_x and overlap_y:
                return True
    return False


def _pack_shelves(
    ordered_indices: list[int],
    extents: list[tuple[float, float]],
    max_row_width: float,
    gap_mm: float,
) -> tuple[list[list[int]], float, float]:
    """Pack `ordered_indices` greedily into horizontal shelves bounded by `max_row_width`."""
    rows: list[list[int]] = []
    cur_row: list[int] = []
    cur_w = 0.0

    for idx in ordered_indices:
        w, _ = extents[idx]
        needed_w = w if not cur_row else (cur_w + gap_mm + w)
        if cur_row and needed_w > max_row_width:
            rows.append(cur_row)
            cur_row = [idx]
            cur_w = w
        else:
            cur_row.append(idx)
            cur_w = needed_w
    if cur_row:
        rows.append(cur_row)

    total_w = 0.0
    total_h = 0.0
    for r_idx, row in enumerate(rows):
        rw = sum(extents[i][0] for i in row) + gap_mm * (len(row) - 1)
        rh = max(extents[i][1] for i in row)
        total_w = max(total_w, rw)
        total_h += rh + (gap_mm if r_idx > 0 else 0.0)

    return rows, total_w, total_h


def _arrange_items_on_bed(extents, z_offsets, bed_x, bed_y, gap_mm=8.0):
    usable_x = bed_x - 8
    usable_y = bed_y - 8
    best = None
    for cap in [usable_x, usable_x * 0.8, usable_x * 0.6]:
        rows, w, h = _pack_shelves(list(range(len(extents))), extents, cap, gap_mm)
        if w <= usable_x and h <= usable_y and (best is None or w * h < best[0]):
            best = (w * h, rows, w, h)
    if best is None:
        raise ValueError(
            "Objects do not fit this print bed; export individual parts or select a larger printer"
        )
    _, rows, w, h = best
    out = [None] * len(extents)
    y = (bed_y - h) / 2
    for row in rows:
        rw = sum(extents[i][0] for i in row) + gap_mm * (len(row) - 1)
        rh = max(extents[i][1] for i in row)
        x = (bed_x - rw) / 2
        for i in row:
            wi, di = extents[i]
            out[i] = (x + wi / 2, y + rh / 2, z_offsets[i])
            x += wi + gap_mm
        y += rh + gap_mm
    return out


def _build_project_settings_dict(
    params: dict[str, Any] | None, host_config: dict[str, Any] | None
) -> dict[str, Any]:
    """Merge host project settings with structural mechanical thread overrides for OrcaSlicer 2.5.1+."""
    merged: dict[str, Any] = {}
    if isinstance(host_config, dict):
        raw_ps = host_config.get("project_settings")
        if isinstance(raw_ps, dict):
            merged.update(raw_ps)

    p = params if isinstance(params, dict) else {}

    # Threaded components are structural mechanical parts: NEVER slice in spiral vase mode!
    merged["spiral_mode"] = "0"
    merged["spiral_mode_smooth"] = "0"

    if bool(p.get("auto_configure_slicer", True)):
        merged["wall_loops"] = "5"
        merged["top_shell_layers"] = "5"
        merged["bottom_shell_layers"] = "5"
        merged["sparse_infill_density"] = "30%"
        merged["sparse_infill_pattern"] = "gyroid"
        merged["layer_height"] = str(
            min(0.16, max(0.06, float(p.get("pitch", 3)) / 12))
        )
        merged["elefant_foot_compensation"] = "0.15"

    return merged


def write_binary_stl(
    path: str | Path, mesh: Any, header_name: str = "OrcaThreadStudio"
) -> Path:
    """Write a duck-typed MeshData object to a standard little-endian binary STL file.

    Binary layout: 80-byte ASCII header + uint32 triangle count + F * 50-byte facet records.
    """
    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    vertices, triangles, normals = _extract_mesh_arrays(mesh)
    num_triangles = int(triangles.shape[0])

    clean_header = str(header_name or "OrcaThreadStudio").strip() or "OrcaThreadStudio"
    if clean_header.lower().startswith("solid"):
        clean_header = f"Orca_{clean_header}"
    header_text = f"{clean_header} - Orca Thread Studio Binary STL"
    header_bytes = header_text.encode("ascii", errors="replace")[:80].ljust(80, b"\x00")

    records = np.zeros(num_triangles, dtype=_STL_RECORD_DTYPE)
    if num_triangles > 0:
        tris_xyz = vertices[triangles]
        records["normal"] = normals.astype("<f4", copy=False)
        records["v0"] = tris_xyz[:, 0, :].astype("<f4", copy=False)
        records["v1"] = tris_xyz[:, 1, :].astype("<f4", copy=False)
        records["v2"] = tris_xyz[:, 2, :].astype("<f4", copy=False)
        records["attr"] = 0

    with open(out_path, "wb") as fh:
        fh.write(header_bytes)
        fh.write(struct.pack("<I", num_triangles))
        if num_triangles > 0:
            fh.write(records.tobytes())

    return out_path


def write_orca_3mf(
    path: str | Path,
    items: list[tuple[str, Any] | tuple[str, Any, tuple[float, float, float] | None]],
    params: dict[str, Any],
    host_config: dict[str, Any] | None = None,
) -> Path:
    """Write an OrcaSlicer 2.5.1+ compatible .3mf project archive with multi-object layout & slicer settings."""
    if not items:
        raise ValueError("write_orca_3mf requires at least one item in 'items'.")

    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    bed_x, bed_y, max_z = _resolve_printable_limits(host_config)
    cx, cy = bed_x * 0.5, bed_y * 0.5

    parsed_items: list[
        tuple[str, np.ndarray, np.ndarray, tuple[float, float], tuple[float, float]]
    ] = []
    raw_positions: list[tuple[float, float, float] | None] = []
    z_offsets: list[float] = []

    for idx, entry in enumerate(items):
        if len(entry) == 2:
            raw_name, mesh = entry  # type: ignore[misc]
            raw_pos = None
        elif len(entry) >= 3:
            raw_name, mesh, raw_pos = entry[0], entry[1], entry[2]
        else:
            raise ValueError(f"Invalid item tuple at index {idx}: {entry!r}")

        raw_item_name = str(raw_name or f"Part_{idx + 1}")
        _validate_xml_text(raw_item_name, "Object name")
        item_name = raw_item_name.strip() or f"Part_{idx + 1}"
        vertices, triangles, _ = _extract_mesh_arrays(mesh)
        ext = _mesh_xy_extents(mesh, vertices)
        local_mid = _mesh_xy_center_offset(mesh, vertices)
        parsed_items.append((item_name, vertices, triangles, ext, local_mid))

        if raw_pos is None:
            raw_positions.append(None)
            z_offsets.append(0.0)
        else:
            px, py, pz = float(raw_pos[0]), float(raw_pos[1]), float(raw_pos[2])
            raw_positions.append((px, py, pz))
            z_offsets.append(pz)

    extents_list = [it[3] for it in parsed_items]
    if any(pos is None for pos in raw_positions):
        box_centers = _arrange_items_on_bed(
            extents_list, z_offsets, bed_x, bed_y, gap_mm=8.0
        )
        # Subtract local mesh midpoint so even asymmetric sector/gauge meshes land centered on their box!
        final_positions = [
            (bx - parsed_items[i][4][0], by - parsed_items[i][4][1], bz)
            for i, (bx, by, bz) in enumerate(box_centers)
        ]
    else:
        concrete_centers = [
            (pos[0] + parsed_items[i][4][0], pos[1] + parsed_items[i][4][1], pos[2])
            for i, pos in enumerate(raw_positions)
            if pos is not None
        ]
        if len(concrete_centers) >= 2 and _positions_overlap(
            concrete_centers, extents_list, min_clearance_mm=3.0
        ):
            box_centers = _arrange_items_on_bed(
                extents_list, z_offsets, bed_x, bed_y, gap_mm=8.0
            )
            final_positions = [
                (bx - parsed_items[i][4][0], by - parsed_items[i][4][1], bz)
                for i, (bx, by, bz) in enumerate(box_centers)
            ]
        else:
            final_positions = [pos for pos in raw_positions if pos is not None]

    for index, (name, vertices, triangles, extent, midpoint) in enumerate(parsed_items):
        tx, ty, tz = final_positions[index]
        placed = vertices + np.array([tx, ty, tz])
        if (
            np.any(placed[:, 0] < 4)
            or np.any(placed[:, 0] > bed_x - 4)
            or np.any(placed[:, 1] < 4)
            or np.any(placed[:, 1] > bed_y - 4)
        ):
            raise ValueError(
                "An object extends beyond the printable bed; export individual parts"
            )
        if np.min(placed[:, 2]) < -0.001 or np.max(placed[:, 2]) > max_z:
            raise ValueError("An object exceeds the printable height")

    raw_title = str(
        (params or {}).get("name") or parsed_items[0][0] or "Orca Thread Studio"
    )
    _validate_xml_text(raw_title, "Project title")
    title = raw_title.strip()
    escaped_title = _xml_escape(title, {'"': "&quot;"})
    today_iso = _dt.date.today().isoformat()
    ns_seed = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    build_uuid = str(uuid.uuid5(ns_seed, f"orca-thread-build-{title}"))

    object_blocks: list[str] = []
    build_items_xml: list[str] = []
    model_settings_objects: list[str] = []
    model_settings_instances: list[str] = []
    model_settings_assemble: list[str] = []

    for idx, (item_name, vertices, triangles, _, _) in enumerate(parsed_items):
        obj_id = idx + 1
        tx, ty, tz = final_positions[idx]
        esc_name = _xml_escape(item_name, {'"': "&quot;"})
        obj_uuid = str(uuid.uuid5(ns_seed, f"orca-thread-obj-{obj_id}-{item_name}"))
        item_uuid = str(uuid.uuid5(ns_seed, f"orca-thread-item-{obj_id}-{item_name}"))

        verts_py = vertices.tolist()
        tris_py = triangles.tolist()

        vertex_lines = "\n".join(
            f'     <vertex x="{vx:.9g}" y="{vy:.9g}" z="{vz:.9g}"/>'
            for vx, vy, vz in verts_py
        )
        triangle_lines = "\n".join(
            f'     <triangle v1="{v1}" v2="{v2}" v3="{v3}"/>' for v1, v2, v3 in tris_py
        )

        object_blocks.append(
            f'  <object id="{obj_id}" p:UUID="{obj_uuid}" name="{esc_name}" type="model">\n'
            f"   <mesh>\n"
            f"    <vertices>\n"
            f"{vertex_lines}\n"
            f"    </vertices>\n"
            f"    <triangles>\n"
            f"{triangle_lines}\n"
            f"    </triangles>\n"
            f"   </mesh>\n"
            f"  </object>"
        )

        transform_3x4 = f"1 0 0 0 1 0 0 0 1 {tx:.4f} {ty:.4f} {tz:.4f}"
        build_items_xml.append(
            f'  <item objectid="{obj_id}" p:UUID="{item_uuid}" transform="{transform_3x4}" printable="1"/>'
        )

        model_settings_objects.append(
            f'  <object id="{obj_id}">\n'
            f'    <metadata key="name" value="{esc_name}"/>\n'
            f'    <metadata key="extruder" value="1"/>\n'
            f'    <part id="1" subtype="normal_part">\n'
            f'      <metadata key="name" value="{esc_name}"/>\n'
            f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
            f'      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
            f"    </part>\n"
            f"  </object>"
        )
        model_settings_instances.append(
            f"    <model_instance>\n"
            f'      <metadata key="object_id" value="{obj_id}"/>\n'
            f'      <metadata key="instance_id" value="0"/>\n'
            f'      <metadata key="identify_id" value="{100 + obj_id}"/>\n'
            f"    </model_instance>"
        )
        model_settings_assemble.append(
            f'    <assemble_item object_id="{obj_id}" instance_id="0" transform="{transform_3x4}" offset="0 0 0"/>'
        )

    model_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<model unit="millimeter" xml:lang="en-US" '
        'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
        'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021" '
        'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" '
        'requiredextensions="p">\n'
        ' <metadata name="Application">OrcaSlicer-2.5.1</metadata>\n'
        ' <metadata name="OrcaSlicer">2.5.1</metadata>\n'
        ' <metadata name="BambuStudio:3mfVersion">1</metadata>\n'
        f' <metadata name="Title">{escaped_title}</metadata>\n'
        f' <metadata name="CreationDate">{today_iso}</metadata>\n'
        " <resources>\n"
        + "\n".join(object_blocks)
        + "\n </resources>\n"
        + f' <build p:UUID="{build_uuid}">\n'
        + "\n".join(build_items_xml)
        + "\n </build>\n"
        "</model>\n"
    )

    model_settings_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<config>\n" + "\n".join(model_settings_objects) + "\n  <plate>\n"
        '    <metadata key="plater_id" value="1"/>\n'
        '    <metadata key="plater_name" value=""/>\n'
        '    <metadata key="locked" value="false"/>\n'
        + "\n".join(model_settings_instances)
        + "\n  </plate>\n"
        "  <assemble>\n" + "\n".join(model_settings_assemble) + "\n  </assemble>\n"
        "</config>\n"
    )

    project_settings = _build_project_settings_dict(params, host_config)
    project_settings_json = json.dumps(project_settings, indent=2, ensure_ascii=False)

    with zipfile.ZipFile(
        out_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6
    ) as zf:
        zf.writestr("[Content_Types].xml", _CONTENT_TYPES_XML)
        zf.writestr("_rels/.rels", _RELS_XML)
        zf.writestr("3D/3dmodel.model", model_xml)
        zf.writestr("Metadata/model_settings.config", model_settings_xml)
        zf.writestr("Metadata/project_settings.config", project_settings_json)

    return out_path

# ===========================================================================
# MODULE: thread_studio.presets_catalog
# ===========================================================================

"""Twelve bilingual starting points and atomic user preset persistence."""

pass  # [bundled] hoisted __future__ import
import json, uuid, random
from pathlib import Path
pass  # [bundled] resolved intra-package import

_PRESET_ROWS = [
    ("edc", "Pote EDC 40", "EDC jar 40", dict()),
    (
        "small",
        "Pote compacto 28",
        "Compact jar 28",
        dict(nominal_dia=28, diameter=32, height=35, pitch=2, thread_length=8),
    ),
    (
        "large",
        "Pote oficina 70",
        "Workshop jar 70",
        dict(nominal_dia=70, diameter=75, height=80, pitch=4),
    ),
    (
        "pco",
        "PET PCO-1881 experimental",
        "PET PCO-1881 experimental",
        dict(module="standard_bottle_cap", standard="pco1881"),
    ),
    (
        "mason70",
        "Mason 70 experimental",
        "Mason 70 experimental",
        dict(module="standard_bottle_cap", standard="mason_70"),
    ),
    (
        "mason86",
        "Mason 86: medir primeiro",
        "Mason 86: measure first",
        dict(module="standard_bottle_cap", standard="mason_86"),
    ),
    (
        "vacuum35",
        "Aspirador 35 para 58",
        "Vacuum 35 to 58",
        dict(module="hose_vacuum_adapter", inlet_diameter=35, outlet_diameter=58),
    ),
    (
        "hose25",
        "Mangueira 25 para 32",
        "Hose 25 to 32",
        dict(
            module="hose_vacuum_adapter",
            inlet_diameter=25,
            outlet_diameter=32,
            end_a="barb",
            end_b="barb",
        ),
    ),
    (
        "adapter",
        "Adaptador rosqueado M40",
        "M40 threaded adapter",
        dict(
            module="hose_vacuum_adapter",
            inlet_diameter=40,
            outlet_diameter=32,
            end_a="female",
            end_b="male",
        ),
    ),
    (
        "m6",
        "Parafuso e porca M6",
        "M6 bolt and nut",
        dict(
            module="bolt_nut_knob",
            standard="iso_metric",
            nominal_dia=6,
            pitch=1,
            thread_length=15,
            head_height=3,
            wall_thickness=1.2,
            gasket=False,
        ),
    ),
    (
        "m12",
        "Manipulo M12",
        "M12 hand knob",
        dict(
            module="bolt_nut_knob",
            standard="iso_metric",
            nominal_dia=12,
            pitch=1.75,
            thread_length=22,
            head="knurled",
            gasket=False,
        ),
    ),
    (
        "wing",
        "Borboleta M20 esquerda",
        "M20 left-hand wing bolt",
        dict(
            module="bolt_nut_knob",
            standard="fdm_trapezoid_45",
            nominal_dia=20,
            pitch=2.5,
            hand="left",
            head="wing",
            gasket=False,
        ),
    ),
]
BUILTIN_PRESETS = [
    dict(id=i, name_pt=pt, name_en=en, params=normalize_params(p))
    for i, pt, en, p in _PRESET_ROWS
]


def load_user_presets(directory):
    f = Path(directory) / "user_presets.json"
    if not f.is_file():
        return []
    data = json.loads(f.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Invalid preset list")
    return [
        dict(
            id=str(x["id"]),
            name=str(x["name"])[:80],
            params=normalize_params(x["params"]),
        )
        for x in data
    ]


def _write_presets(directory, data):
    d = Path(directory)
    d.mkdir(parents=True, exist_ok=True)
    f = d / "user_presets.json"
    temp = d / "user_presets.tmp"
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(f)
    return data


def save_user_preset(directory, name, params, preset_id=None):
    data = load_user_presets(directory)
    pid = str(preset_id or uuid.uuid4().hex)
    data = [x for x in data if x["id"] != pid]
    data.append(dict(id=pid, name=str(name)[:80], params=normalize_params(params)))
    return _write_presets(directory, data)


def delete_user_preset(directory, preset_id):
    return _write_presets(
        directory,
        [x for x in load_user_presets(directory) if x["id"] != str(preset_id)],
    )


def generate_random_printable_params(seed=None, current_params=None):
    """Explore the current family without granting experimental confirmations.

    Bottle-standard dimensions stay fixed by normalization. An unconfirmed
    Mason 86 design deliberately remains blocked until a human checks it.
    """
    rng = random.Random(seed)
    candidate = dict(current_params or {})
    candidate["measurements_confirmed"] = False
    p = normalize_params(candidate)
    p.update(
        texture=rng.choice(["knurled", "fluted", "smooth", "faceted"]),
        knurl_depth=rng.choice([0.2, 0.4, 0.6]),
        knurl_count=rng.choice([24, 32, 40, 48]),
        diametral_clearance=rng.choice([0.18, 0.22, 0.26, 0.30]),
        axial_clearance=rng.choice([0.08, 0.12, 0.16]),
        higbee_turns=rng.choice([0.45, 0.6, 0.75]),
        wall_thickness=rng.choice([1.6, 2.0, 2.4]),
        floor_thickness=rng.choice([1.6, 2.0, 2.4]),
    )
    family = p["module"]
    if family == "container_and_lid":
        diameter = rng.choice([28.0, 32.0, 40.0, 48.0, 60.0])
        pitch = rng.choice([2.0, 2.5, 3.0])
        p.update(
            nominal_dia=diameter,
            diameter=diameter + 6,
            height=rng.choice([40.0, 50.0, 65.0, 80.0]),
            pitch=pitch,
            thread_length=pitch * rng.choice([3, 4, 5]),
            starts=rng.choice([1, 2, 3]),
        )
    elif family == "standard_bottle_cap":
        if p["standard"] in ("iso_metric", "fdm_trapezoid_45"):
            p.update(
                nominal_dia=rng.choice([24.0, 28.0, 32.0, 40.0, 50.0]),
                pitch=rng.choice([2.0, 2.5, 3.0]),
                thread_length=rng.choice([8.0, 10.0, 12.0]),
            )
        # PCO/Mason nominal dimensions and all measured values remain intact.
    elif family == "hose_vacuum_adapter":
        p.update(
            inlet_diameter=rng.choice([25.0, 32.0, 35.0, 40.0]),
            outlet_diameter=rng.choice([32.0, 40.0, 50.0, 58.0]),
            adapter_length=rng.choice([45.0, 60.0, 75.0, 90.0]),
            end_length=rng.choice([10.0, 12.0, 15.0]),
            end_a=rng.choice(["smooth", "barb", "male", "female"]),
            end_b=rng.choice(["smooth", "barb", "male", "female"]),
            pitch=rng.choice([2.0, 2.5, 3.0]),
        )
    else:
        p.update(
            nominal_dia=rng.choice([12.0, 16.0, 20.0, 24.0, 32.0]),
            pitch=rng.choice([1.5, 2.0, 2.5]),
            thread_length=rng.choice([15.0, 20.0, 25.0, 30.0]),
            head=rng.choice(["hex", "knurled", "wing"]),
            head_height=rng.choice([4.0, 5.0, 6.0]),
            bore_diameter=0.0,
            gasket=False,
        )
    p["measurements_confirmed"] = False
    return normalize_params(p)

# ===========================================================================
# MODULE: thread_studio.studio_ui
# ===========================================================================

"""Offline Thread Studio on the canonical Orca Vase Studio interface template.

Common CSS, layout, controls and studio materials derive from Orca Vase Studio
under MIT; models displayed here are the native Thread Studio mesh arrays.
"""

pass  # [bundled] hoisted __future__ import
import copy
import json
from html import escape
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import


def get_studio_html(mode="page", initial_context=None):
    context = copy.deepcopy(initial_context or {})
    context["params"] = normalize_params(context.get("params", DEFAULT_PARAMS))
    context.setdefault("builtin_presets", BUILTIN_PRESETS)
    context.setdefault("user_presets", [])
    context["mode"] = "dock" if mode == "dock" else "page"
    context["lang"] = normalize_language(context.get("lang", context["params"]["lang"]))
    context["languages"] = LANGUAGE_METADATA
    context["translations"] = TRANSLATIONS
    context["theme"] = (
        "light"
        if context.get("theme", context["params"]["theme"]) == "light"
        else "dark"
    )
    context["params"]["lang"] = context["lang"]
    context["params"]["theme"] = context["theme"]
    payload = (
        json.dumps(context, ensure_ascii=False, separators=(",", ":"))
        .replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    return (
        _HTML.replace("__THREAD_BOOT_JSON__", payload)
        .replace("__THREAD_LANGUAGE_OPTIONS__", "".join(
            f'<option value="{escape(m["code"], quote=True)}">{escape(m["native_name"])}</option>'
            for m in LANGUAGE_METADATA))
        .replace("__INITIAL_LANG__", context["lang"])
        .replace("__INITIAL_THEME__", context["theme"])
        .replace("__INITIAL_MODE__", context["mode"])
    )


_HTML = __import__('zlib').decompress(__import__('base64').b64decode(b'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')).decode('utf-8')

# ===========================================================================
# MODULE: thread_studio.linux_ipc
# ===========================================================================

"""OrcaSlicer session-bus transport. No subprocess or third-party package.

Protocol reference: OrcaSlicer v2.5.1 src/slic3r/GUI/InstanceCheck.cpp.
Transport completion does not confirm the host has loaded the objects.
"""

pass  # [bundled] hoisted __future__ import

import ctypes
import os
import re
import sys


def send_linux_plater_request(
    payload: str, *, process_id: int | None = None
) -> tuple[bool, str]:
    """Send only to the Orca instance hosted in this process (or explicit PID)."""
    if not sys.platform.startswith("linux"):
        return False, "Linux session D-Bus transport is unavailable on this platform."
    if not isinstance(payload, str) or not payload or "\x00" in payload:
        return False, "The import request must be a nonempty string without NUL."
    connection = None
    library = None
    try:
        library = ctypes.CDLL("libdbus-1.so.3")
        pointer = ctypes.c_void_p
        string = ctypes.c_char_p
        uint = ctypes.c_uint32
        signatures = {
            "dbus_threads_init_default": (ctypes.c_int, []),
            "dbus_bus_get_private": (pointer, [ctypes.c_int, pointer]),
            "dbus_connection_set_exit_on_disconnect": (None, [pointer, ctypes.c_int]),
            "dbus_message_new_method_call": (pointer, [string, string, string, string]),
            "dbus_message_append_args": (ctypes.c_int, [pointer, ctypes.c_int]),
            "dbus_message_get_args": (ctypes.c_int, [pointer, pointer, ctypes.c_int]),
            "dbus_connection_send_with_reply_and_block": (
                pointer,
                [pointer, pointer, ctypes.c_int, pointer],
            ),
            "dbus_message_get_type": (ctypes.c_int, [pointer]),
            "dbus_message_set_no_reply": (None, [pointer, ctypes.c_int]),
            "dbus_message_set_auto_start": (None, [pointer, ctypes.c_int]),
            "dbus_connection_send": (
                ctypes.c_int,
                [pointer, pointer, ctypes.POINTER(uint)],
            ),
            "dbus_connection_flush": (None, [pointer]),
            "dbus_connection_get_is_connected": (ctypes.c_int, [pointer]),
            "dbus_message_unref": (None, [pointer]),
            "dbus_connection_close": (None, [pointer]),
            "dbus_connection_unref": (None, [pointer]),
            "dbus_free_string_array": (None, [ctypes.POINTER(string)]),
        }
        for name, (result, arguments) in signatures.items():
            function = getattr(library, name)
            function.restype = result
            function.argtypes = arguments
        if not library.dbus_threads_init_default():
            return False, "Unable to initialize D-Bus threading."
        connection = library.dbus_bus_get_private(0, None)
        if not connection:
            return False, "No usable session D-Bus connection; export a 3MF instead."
        library.dbus_connection_set_exit_on_disconnect(connection, 0)

        def daemon_call(method: bytes, argument: str | None = None):
            request = library.dbus_message_new_method_call(
                b"org.freedesktop.DBus",
                b"/org/freedesktop/DBus",
                b"org.freedesktop.DBus",
                method,
            )
            if not request:
                raise RuntimeError("Cannot allocate D-Bus request.")
            try:
                if argument is not None:
                    encoded = string(argument.encode("utf-8"))
                    if not library.dbus_message_append_args(
                        request, ord("s"), ctypes.byref(encoded), ctypes.c_int(0)
                    ):
                        raise RuntimeError("Cannot encode D-Bus request.")
                reply = library.dbus_connection_send_with_reply_and_block(
                    connection, request, 1500, None
                )
                if not reply:
                    raise RuntimeError("D-Bus daemon request timed out or failed.")
                if library.dbus_message_get_type(reply) != 2:
                    library.dbus_message_unref(reply)
                    raise RuntimeError("D-Bus daemon rejected the request.")
                return reply
            finally:
                library.dbus_message_unref(request)

        reply = daemon_call(b"ListNames")
        names = ctypes.POINTER(string)()
        count = ctypes.c_int()
        try:
            if not library.dbus_message_get_args(
                reply,
                None,
                ord("a"),
                ctypes.c_int(ord("s")),
                ctypes.byref(names),
                ctypes.byref(count),
                ctypes.c_int(0),
            ):
                raise RuntimeError("Invalid D-Bus service listing.")
            candidates = [names[i].decode("utf-8") for i in range(count.value)]
        finally:
            if names:
                library.dbus_free_string_array(names)
            library.dbus_message_unref(reply)
        expected_pid = os.getpid() if process_id is None else int(process_id)
        owned = []
        for name in candidates:
            if not re.fullmatch(
                r"com\.orcaslicer\.OrcaSlicer\.InstanceCheck\.Object[0-9]+", name
            ):
                continue
            try:
                reply = daemon_call(b"GetNameOwner", name)
                unique_owner = string()
                try:
                    valid = library.dbus_message_get_args(
                        reply,
                        None,
                        ord("s"),
                        ctypes.byref(unique_owner),
                        ctypes.c_int(0),
                    )
                    if not valid or not unique_owner.value:
                        continue
                    owner = unique_owner.value.decode("utf-8")
                finally:
                    library.dbus_message_unref(reply)
                reply = daemon_call(b"GetConnectionUnixProcessID", owner)
            except RuntimeError:
                continue
            pid = uint()
            try:
                valid = library.dbus_message_get_args(
                    reply, None, ord("u"), ctypes.byref(pid), ctypes.c_int(0)
                )
                if valid and pid.value == expected_pid:
                    owned.append((name, owner))
            finally:
                library.dbus_message_unref(reply)
        if len(owned) != 1:
            return (
                False,
                "Unable to identify exactly one OrcaSlicer service for this process; export a 3MF instead.",
            )
        interface, destination = owned[0]
        suffix = interface.rsplit("Object", 1)[1]
        request = library.dbus_message_new_method_call(
            destination.encode("ascii"),
            ("/com/orcaslicer/OrcaSlicer/InstanceCheck/Object" + suffix).encode(
                "ascii"
            ),
            interface.encode("ascii"),
            b"AnotherInstance",
        )
        if not request:
            return False, "Unable to allocate the import request."
        try:
            encoded = string(payload.encode("utf-8"))
            if not library.dbus_message_append_args(
                request, ord("s"), ctypes.byref(encoded), ctypes.c_int(0)
            ):
                return False, "Unable to encode the import request."
            library.dbus_message_set_no_reply(request, 1)
            library.dbus_message_set_auto_start(request, 0)
            serial = uint()
            if not library.dbus_connection_send(
                connection, request, ctypes.byref(serial)
            ):
                return False, "D-Bus could not queue the import request."
            library.dbus_connection_flush(connection)
            if not library.dbus_connection_get_is_connected(connection):
                return False, "D-Bus disconnected while sending the import request."
            return True, "Import request sent; object loading has not been confirmed."
        finally:
            library.dbus_message_unref(request)
    except (OSError, AttributeError, RuntimeError, ValueError) as error:
        return False, "Linux import unavailable: " + str(error)
    finally:
        if connection and library is not None:
            library.dbus_connection_close(connection)
            library.dbus_connection_unref(connection)

# ===========================================================================
# MODULE: thread_studio.plugin_main
# ===========================================================================

pass  # [bundled] hoisted __future__ import

from collections.abc import Sequence
import copy
import ctypes
import json
import locale
import os
import re
import sys
import threading
import time
import types
import uuid
from pathlib import Path
from typing import Any, Callable

pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
import numpy as np


def _build_fallback_orca_module() -> types.ModuleType:
    """Create a lightweight stand-in when imported outside OrcaSlicer."""
    mod = types.ModuleType("orca")
    mod._registered_capabilities = []
    mod._requested_permissions = {}
    mod._plugin_cls = None

    class PythonPluginBase:
        def __init__(self) -> None:
            self._stored_config: str = "{}"

        def get_name(self) -> str:
            return ""

        def on_load(self) -> None:
            pass

        def on_unload(self) -> None:
            pass

        def has_config_ui(self) -> bool:
            return False

        def get_config_ui(self) -> str:
            return ""

        def get_default_config(self) -> dict[str, Any]:
            return {}

        def get_config(self) -> str:
            return self._stored_config

        def get_config_version(self) -> str:
            return "1.0.0"

        def save_config(self, config: str) -> bool:
            self._stored_config = str(config or "{}")
            return True

    class BasePlugin:
        def __init__(self) -> None:
            pass

        def register_capabilities(self) -> None:
            pass

    class PagesPluginCapabilityBase(PythonPluginBase):
        def get_ui(self) -> str:
            return ""

        def get_icon(self) -> str:
            return ""

        def on_message(self, data: Any) -> None:
            pass

        def post_message(self, data: Any) -> None:
            pass

    class ScriptPluginCapabilityBase(PythonPluginBase):
        def execute(self) -> Any:
            return None

    class PluginResult:
        Success = 0
        Skipped = 1
        RecoverableError = 2
        FatalError = 3

    class ExecutionResult:
        def __init__(self, status: int = 0, message: str = "", data: str = "") -> None:
            self.status = status
            self.message = message
            self.data = data

        @classmethod
        def success(cls, message: str = "", data: str = "") -> "ExecutionResult":
            return cls(PluginResult.Success, message, data)

        @classmethod
        def skipped(cls, message: str = "") -> "ExecutionResult":
            return cls(PluginResult.Skipped, message, "")

        @classmethod
        def failure(
            cls, status: int, message: str, data: str = ""
        ) -> "ExecutionResult":
            return cls(status, message, data)

    def plugin_decorator(cls: type) -> type:
        mod._plugin_cls = cls
        return cls

    def register_capability(cap_cls: type) -> None:
        mod._registered_capabilities.append(cap_cls)

    def request_permissions(**kwargs: Any) -> None:
        mod._requested_permissions.update(kwargs)

    pages_mod = types.ModuleType("orca.pages")
    pages_mod.PagesPluginCapabilityBase = PagesPluginCapabilityBase

    script_mod = types.ModuleType("orca.script")
    script_mod.ScriptPluginCapabilityBase = ScriptPluginCapabilityBase

    plugin_sub = types.ModuleType("orca.plugin")
    plugin_sub.storage = lambda: str(
        _orca_user_config_root() / "plugin_data" / "orca_thread_generator"
    )

    class NotificationLevel:
        RegularNotificationLevel = 0
        HintNotificationLevel = 1
        ProgressBarNotificationLevel = 2
        PrintInfoNotificationLevel = 3
        PrintInfoShortNotificationLevel = 4
        ImportantNotificationLevel = 5
        WarningNotificationLevel = 6
        SeriousWarningNotificationLevel = 7
        ErrorNotificationLevel = 8

    host_mod = types.ModuleType("orca.host")
    host_mod.app_language = lambda: "pt_BR"
    host_mod.app_info = lambda: {"version": "2.5.1", "language": "pt_BR"}
    host_mod.preset_bundle = lambda: None
    host_mod.plater = lambda: None
    host_mod.model = lambda: None
    host_mod.selected_printer = lambda: None
    host_mod.plugin = plugin_sub
    host_mod.ui = types.SimpleNamespace(
        NotificationLevel=NotificationLevel,
        create_dock_panel=None,
        create_window=None,
        push_notification=None,
        message=None,
    )
    host_mod.preset = types.SimpleNamespace(
        process=None,
        printer=None,
        filament=None,
    )

    mod.base = BasePlugin
    mod.PythonPluginBase = PythonPluginBase
    mod.PluginResult = PluginResult
    mod.ExecutionResult = ExecutionResult
    mod.plugin = plugin_decorator
    mod.register_capability = register_capability
    mod.request_permissions = request_permissions
    mod.pages = pages_mod
    mod.script = script_mod
    mod.host = host_mod

    return mod


try:
    import orca  # type: ignore[import-not-found]
except ImportError:
    orca = _build_fallback_orca_module()


PLUGIN_SLUG = "orca_thread_generator"
WM_COPYDATA = 0x004A
SMTO_ABORTIFHUNG = 0x0002
ORCA_OTHER_INSTANCE_DWDATA = 1

ICON_SVG_CONTENT = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64"><defs><linearGradient id="thread" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#80ffea"/><stop offset="1" stop-color="#00897b"/></linearGradient></defs><ellipse cx="32" cy="55" rx="25" ry="5" fill="none" stroke="#00bfa5" opacity=".5"/><path d="M18 17l14-7 14 7v29l-14 8-14-8z" fill="#17252b" stroke="url(#thread)" stroke-width="2"/><path d="M19 23l26-9m-26 16l26-9m-26 16l26-9m-26 16l26-9m-26 16l26-9" fill="none" stroke="url(#thread)" stroke-width="4" stroke-linejoin="round"/><path d="M27 7h10v8H27z" fill="#ffb74d"/></svg>'

# ---------------------------------------------------------------------------
# Cross-Platform Environment, Storage & In-Process Plater IPC (Win32 + macOS)
# ---------------------------------------------------------------------------

_MACOS_PENDING_DISPATCH_CBS: list[Any] = []


def _is_native_orca_host() -> bool:
    """Return True only when running inside the real C++ pybind11 OrcaSlicer host."""
    base_cls = getattr(orca, "base", None)
    return base_cls is not None and type(base_cls).__name__ == "pybind11_type"


def _is_mock_callable(obj: Any) -> bool:
    """Detect unittest.mock objects without importing unittest.mock eagerly."""
    cls_mod = getattr(type(obj), "__module__", "")
    return cls_mod.startswith("unittest.mock")


def _orca_user_config_root(platform_name: str | None = None) -> Path:
    """Return OrcaSlicer's user configuration directory on Windows, macOS, and Linux."""
    plat = platform_name or sys.platform
    if plat == "win32":
        appdata = os.environ.get("APPDATA", "").strip()
        if appdata:
            return Path(appdata) / "OrcaSlicer"
        return Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    if plat == "darwin":
        return Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    base = Path(xdg) if xdg else (Path.home() / ".config")
    return base / "OrcaSlicer"


def _default_installed_plugin_dir() -> Path:
    return _orca_user_config_root() / "orca_plugins" / PLUGIN_SLUG


def _default_plugin_data_dir() -> Path:
    return _orca_user_config_root() / "orca_plugins" / "plugin_data" / PLUGIN_SLUG


def _resolve_storage_dir() -> Path:
    """Resolve current plugin storage folder safely (inside or outside callbacks)."""
    # 1. Try orca.plugin.storage() or orca.host.plugin.storage()
    for holder in (
        getattr(orca, "plugin", None),
        getattr(getattr(orca, "host", None), "plugin", None),
    ):
        storage_fn = getattr(holder, "storage", None)
        if callable(storage_fn):
            try:
                raw = storage_fn()
                if isinstance(raw, (str, os.PathLike)) and str(raw).strip():
                    return Path(raw)
            except Exception:
                pass

    # 2. In native OrcaSlicer, prefer `plugin_data/orca_thread_generator`
    if _is_native_orca_host():
        data_dir = _default_plugin_data_dir()
        try:
            data_dir.mkdir(parents=True, exist_ok=True)
            return data_dir
        except Exception:
            pass

    # 3. Fallback to __file__ parent if available
    try:
        here = Path(__file__).resolve().parent
        if here.exists():
            return here
    except Exception:
        pass

    return _default_installed_plugin_dir()


def _format_other_instance_payload(file_paths: Sequence[str | Path]) -> str:
    """Format Win32 `WM_COPYDATA` payload matching `OrcaSlicer.dll` `unescape_strings_cstyle`.

    Produces `"orca-slicer.exe";"<resolved_path_1>";...` where every token escapes
    `\\` -> `\\\\`, `"` -> `\\"`, `\\r` -> `\\r`, `\\n` -> `\\n`, wrapped in double quotes and
    joined by `;` with NO trailing `;` (`OtherInstanceMessageHandler::handle_message` skips `args[0]`).
    """
    resolved_files = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved_files:
        raise ValueError("file_paths must contain at least one model path")

    tokens = ["orca-slicer.exe", *resolved_files]
    escaped: list[str] = []
    for tok in tokens:
        s = (
            tok.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\r", "\\r")
            .replace("\n", "\\n")
        )
        escaped.append(f'"{s}"')
    return ";".join(escaped)


def _find_orca_mainframe_hwnd(target_pid: int | None = None) -> int | None:
    """Locate OrcaSlicer's `MainFrame` `wxWindowNR` `HWND` in `target_pid` (`os.getpid()` by default).

    Prefers `wxWindowNR` windows marked with OrcaSlicer's `Instance_Hash_Minor` or
    `Instance_Hash_Major` properties, falling back to a visible top-level `wxWindowNR` of that PID.
    """
    if sys.platform != "win32":
        return None

    from ctypes import wintypes

    pid = int(target_pid) if target_pid is not None else os.getpid()
    user32 = ctypes.windll.user32

    WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    enum_windows = user32.EnumWindows
    if not _is_mock_callable(enum_windows):
        enum_windows.argtypes = [WNDENUMPROC, wintypes.LPARAM]
        enum_windows.restype = wintypes.BOOL

    get_pid = user32.GetWindowThreadProcessId
    if not _is_mock_callable(get_pid):
        get_pid.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
        get_pid.restype = wintypes.DWORD

    get_class = user32.GetClassNameW
    if not _is_mock_callable(get_class):
        get_class.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
        get_class.restype = ctypes.c_int

    get_prop = user32.GetPropW
    if not _is_mock_callable(get_prop):
        get_prop.argtypes = [wintypes.HWND, wintypes.LPCWSTR]
        get_prop.restype = wintypes.HANDLE

    is_visible = user32.IsWindowVisible
    if not _is_mock_callable(is_visible):
        is_visible.argtypes = [wintypes.HWND]
        is_visible.restype = wintypes.BOOL

    get_parent = user32.GetParent
    if not _is_mock_callable(get_parent):
        get_parent.argtypes = [wintypes.HWND]
        get_parent.restype = wintypes.HWND

    hash_visible: list[int] = []
    hash_any: list[int] = []
    fallback_visible: list[int] = []

    def _enum_cb(hwnd: int, _lparam: int) -> bool:
        if not hwnd:
            return True
        win_pid = wintypes.DWORD(0)
        get_pid(hwnd, ctypes.byref(win_pid))
        if int(win_pid.value) != pid:
            return True

        cls_buf = ctypes.create_unicode_buffer(64)
        cls_len = get_class(hwnd, cls_buf, 64)
        if cls_len <= 0 or cls_buf.value != "wxWindowNR":
            return True

        minor = get_prop(hwnd, "Instance_Hash_Minor")
        major = get_prop(hwnd, "Instance_Hash_Major")
        vis = bool(is_visible(hwnd))
        hwnd_int = int(hwnd)

        if bool(minor) or bool(major):
            if vis:
                hash_visible.append(hwnd_int)
            else:
                hash_any.append(hwnd_int)
        elif vis and not get_parent(hwnd):
            fallback_visible.append(hwnd_int)
        return True

    cb_ref = WNDENUMPROC(_enum_cb)
    enum_windows(cb_ref, 0)

    if hash_visible:
        return hash_visible[0]
    if hash_any:
        return hash_any[0]
    if fallback_visible:
        return fallback_visible[0]
    return None


class _COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_size_t),
        ("cbData", ctypes.c_uint32),
        ("lpData", ctypes.c_void_p),
    ]


def _dispatch_copydata_to_hwnd(
    hwnd: int,
    payload_str: str,
    timeout_ms: int = 5000,
) -> tuple[bool, str]:
    """Send UTF-16LE `WM_COPYDATA` (`dwData = 1`) to `hwnd` via `SendMessageTimeoutW` (`0x0002`)."""
    if not hwnd or int(hwnd) <= 0:
        return (False, "OrcaSlicer MainFrame HWND not found")
    if not payload_str:
        return (False, "Empty WM_COPYDATA payload")
    if sys.platform != "win32":
        return (False, "WM_COPYDATA requires win32")

    from ctypes import wintypes

    wchar_buf = ctypes.create_unicode_buffer(payload_str)
    cds = _COPYDATASTRUCT(
        dwData=ORCA_OTHER_INSTANCE_DWDATA,
        cbData=ctypes.sizeof(wchar_buf),
        lpData=ctypes.cast(wchar_buf, ctypes.c_void_p),
    )
    result = ctypes.c_size_t(0)

    user32 = ctypes.windll.user32
    send_msg = user32.SendMessageTimeoutW
    if not _is_mock_callable(send_msg):
        send_msg.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            ctypes.c_void_p,
            wintypes.UINT,
            wintypes.UINT,
            ctypes.POINTER(ctypes.c_size_t),
        ]
        send_msg.restype = ctypes.c_size_t

    ret = send_msg(
        int(hwnd),
        WM_COPYDATA,
        0,
        ctypes.byref(cds),
        SMTO_ABORTIFHUNG,
        max(100, int(timeout_ms)),
        ctypes.byref(result),
    )
    if not ret:
        err = ctypes.windll.kernel32.GetLastError()
        return (False, f"SendMessageTimeoutW failed (GetLastError={err})")
    return (True, "ok")


class _MacDispatchQueueS(ctypes.Structure):
    pass


def _load_macos_objc_and_gcd() -> tuple[Any, Any]:
    """Load Objective-C runtime (`libobjc`) and GCD (`libSystem`) on macOS (`arm64` & `x86_64`)."""
    for fw in (
        "/System/Library/Frameworks/Foundation.framework/Foundation",
        "/System/Library/Frameworks/AppKit.framework/AppKit",
    ):
        try:
            ctypes.CDLL(fw)
        except OSError:
            pass

    objc = None
    for cand in ("/usr/lib/libobjc.A.dylib", "libobjc.A.dylib", "libobjc.dylib"):
        try:
            objc = ctypes.CDLL(cand)
            break
        except OSError:
            continue
    if objc is None:
        raise RuntimeError("Could not load macOS libobjc.A.dylib")

    libsystem = None
    for cand in ("/usr/lib/libSystem.B.dylib", "libSystem.B.dylib", "libSystem.dylib"):
        try:
            libsystem = ctypes.CDLL(cand)
            break
        except OSError:
            continue
    if libsystem is None:
        raise RuntimeError("Could not load macOS libSystem.B.dylib")

    if not _is_mock_callable(objc.objc_getClass):
        objc.objc_getClass.argtypes = [ctypes.c_char_p]
        objc.objc_getClass.restype = ctypes.c_void_p
    if not _is_mock_callable(objc.sel_registerName):
        objc.sel_registerName.argtypes = [ctypes.c_char_p]
        objc.sel_registerName.restype = ctypes.c_void_p

    return objc, libsystem


def _resolve_macos_app_bundle_path() -> str | None:
    """Find running `.app` bundle path on macOS from `sys.executable` or `/Applications`."""
    try:
        exe_resolved = Path(sys.executable).resolve()
        for parent in exe_resolved.parents:
            if parent.suffix.lower() == ".app" and parent.is_dir():
                return str(parent)
    except Exception:
        pass

    for cand in (
        Path("/Applications/OrcaSlicer.app"),
        Path.home() / "Applications" / "OrcaSlicer.app",
    ):
        try:
            if cand.is_dir():
                return str(cand)
        except Exception:
            continue
    return None


def _dispatch_macos_open_files(
    file_paths: Sequence[str | Path],
    timeout_ms: int = 5000,
) -> tuple[bool, str]:
    """Send model files in-process to OrcaSlicer's Cocoa `wxAppController` on macOS (`darwin`).

    Marshals onto the Cocoa main queue (`_dispatch_main_q`) using ARM64-safe typed `CFUNCTYPE`
    wrappers around `objc_msgSend`, invoking `[NSApp.delegate application:NSApp openFiles:paths]`
    (`GUI_App::MacOpenFiles` -> `Plater::load_files`), with `NSWorkspace` fallback if needed.
    Requires ZERO external `subprocess` permissions.
    """
    if sys.platform != "darwin":
        return (False, "Cocoa openFiles dispatch requires darwin")

    resolved_files = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved_files:
        return (False, "Empty file_paths for macOS Plater dispatch")

    try:
        objc, libsystem = _load_macos_objc_and_gcd()
    except Exception as exc:
        return (False, f"macOS Objective-C load error: {exc}")

    msg_addr = ctypes.cast(objc.objc_msgSend, ctypes.c_void_p).value
    if not msg_addr:
        return (False, "objc_msgSend address unavailable")

    # Non-variadic ARM64 & x86_64 ABI-safe Objective-C message wrappers
    msg_id0 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(
        msg_addr
    )
    msg_void0 = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)(msg_addr)
    msg_id_cstr = ctypes.CFUNCTYPE(
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p
    )(msg_addr)
    msg_id_id = ctypes.CFUNCTYPE(
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_void_id = ctypes.CFUNCTYPE(
        None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_bool_sel = ctypes.CFUNCTYPE(
        ctypes.c_byte, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_bool_id_id = ctypes.CFUNCTYPE(
        ctypes.c_byte,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
    )(msg_addr)
    msg_void_id_id = ctypes.CFUNCTYPE(
        None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_open_urls = ctypes.CFUNCTYPE(
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_ulong,
        ctypes.c_void_p,
        ctypes.c_void_p,
    )(msg_addr)

    cls_pool = objc.objc_getClass(b"NSAutoreleasePool")
    cls_app = objc.objc_getClass(b"NSApplication")
    cls_str = objc.objc_getClass(b"NSString")
    cls_url = objc.objc_getClass(b"NSURL")
    cls_arr = objc.objc_getClass(b"NSMutableArray")
    cls_ws = objc.objc_getClass(b"NSWorkspace")
    cls_bundle = objc.objc_getClass(b"NSBundle")

    sel_alloc = objc.sel_registerName(b"alloc")
    sel_init = objc.sel_registerName(b"init")
    sel_drain = objc.sel_registerName(b"drain")
    sel_shared_app = objc.sel_registerName(b"sharedApplication")
    sel_delegate = objc.sel_registerName(b"delegate")
    sel_responds = objc.sel_registerName(b"respondsToSelector:")
    sel_open_files = objc.sel_registerName(b"application:openFiles:")
    sel_open_file = objc.sel_registerName(b"application:openFile:")
    sel_str_utf8 = objc.sel_registerName(b"stringWithUTF8String:")
    sel_file_url = objc.sel_registerName(b"fileURLWithPath:")
    sel_array = objc.sel_registerName(b"array")
    sel_add_obj = objc.sel_registerName(b"addObject:")
    sel_shared_ws = objc.sel_registerName(b"sharedWorkspace")
    sel_main_bundle = objc.sel_registerName(b"mainBundle")
    sel_bundle_url = objc.sel_registerName(b"bundleURL")
    sel_open_urls = objc.sel_registerName(
        b"openURLs:withApplicationAtURL:options:configuration:error:"
    )

    done_evt = threading.Event()
    result_box: dict[str, Any] = {
        "ok": False,
        "msg": "macOS main-queue callback pending",
    }

    DISPATCH_FN = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

    def _run_on_cocoa_main(_ctx: int) -> None:
        pool = msg_id0(msg_id0(cls_pool, sel_alloc), sel_init) if cls_pool else None
        try:
            ns_paths = msg_id0(cls_arr, sel_array)
            ns_urls = msg_id0(cls_arr, sel_array)
            for fp in resolved_files:
                ns_s = msg_id_cstr(cls_str, sel_str_utf8, fp.encode("utf-8"))
                if ns_s:
                    msg_void_id(ns_paths, sel_add_obj, ns_s)
                    if cls_url:
                        ns_u = msg_id_id(cls_url, sel_file_url, ns_s)
                        if ns_u:
                            msg_void_id(ns_urls, sel_add_obj, ns_u)

            ns_app = msg_id0(cls_app, sel_shared_app) if cls_app else None
            delegate = msg_id0(ns_app, sel_delegate) if ns_app else None

            if delegate and bool(msg_bool_sel(delegate, sel_responds, sel_open_files)):
                msg_void_id_id(delegate, sel_open_files, ns_app, ns_paths)
                result_box["ok"] = True
                result_box["msg"] = "ok (NSApp.delegate application:openFiles:)"
                return

            if delegate and bool(msg_bool_sel(delegate, sel_responds, sel_open_file)):
                all_ok = True
                for fp in resolved_files:
                    ns_s = msg_id_cstr(cls_str, sel_str_utf8, fp.encode("utf-8"))
                    if not bool(msg_bool_id_id(delegate, sel_open_file, ns_app, ns_s)):
                        all_ok = False
                if all_ok:
                    result_box["ok"] = True
                    result_box["msg"] = "ok (NSApp.delegate application:openFile:)"
                    return

            # Fallback to NSWorkspace openURLs with running bundle URL
            ws = msg_id0(cls_ws, sel_shared_ws) if cls_ws else None
            app_url = None
            if cls_bundle:
                mb = msg_id0(cls_bundle, sel_main_bundle)
                if mb:
                    app_url = msg_id0(mb, sel_bundle_url)
            if not app_url:
                app_path = _resolve_macos_app_bundle_path()
                if app_path and cls_url:
                    ns_app_s = msg_id_cstr(
                        cls_str, sel_str_utf8, app_path.encode("utf-8")
                    )
                    app_url = msg_id_id(cls_url, sel_file_url, ns_app_s)
            if ws and app_url and ns_urls:
                run_app = msg_open_urls(
                    ws, sel_open_urls, ns_urls, app_url, 0, None, None
                )
                if run_app:
                    result_box["ok"] = True
                    result_box["msg"] = "ok (NSWorkspace openURLs)"
                    return

            result_box["ok"] = False
            result_box["msg"] = (
                "No Cocoa openFiles delegate or NSWorkspace target responded"
            )
        except Exception as inner_exc:
            result_box["ok"] = False
            result_box["msg"] = f"Cocoa main-queue exception: {inner_exc}"
        finally:
            if pool:
                try:
                    msg_void0(pool, sel_drain)
                except Exception:
                    pass
            done_evt.set()

    c_cb = DISPATCH_FN(_run_on_cocoa_main)
    _MACOS_PENDING_DISPATCH_CBS.append(c_cb)

    try:
        main_q = ctypes.cast(
            ctypes.byref(_MacDispatchQueueS.in_dll(libsystem, "_dispatch_main_q")),
            ctypes.c_void_p,
        )
        dispatch_async_f = libsystem.dispatch_async_f
        if not _is_mock_callable(dispatch_async_f):
            dispatch_async_f.argtypes = [ctypes.c_void_p, ctypes.c_void_p, DISPATCH_FN]
            dispatch_async_f.restype = None
        dispatch_async_f(main_q, None, c_cb)
    except Exception as exc:
        if c_cb in _MACOS_PENDING_DISPATCH_CBS:
            _MACOS_PENDING_DISPATCH_CBS.remove(c_cb)
        return (False, f"dispatch_async_f failed: {exc}")

    finished = done_evt.wait(timeout=max(0.2, float(timeout_ms) / 1000.0))
    if finished and c_cb in _MACOS_PENDING_DISPATCH_CBS:
        _MACOS_PENDING_DISPATCH_CBS.remove(c_cb)

    if not finished:
        return (False, "Timed out waiting for Cocoa main-queue openFiles")
    return (bool(result_box["ok"]), str(result_box["msg"]))


def _open_folder_native(folder_path: Path) -> bool:
    """Open `folder_path` in Explorer (Windows) or Finder (macOS) without `subprocess`."""
    resolved = str(Path(folder_path).resolve())
    if sys.platform == "win32":
        startfile_fn = getattr(os, "startfile", None)
        if callable(startfile_fn):
            startfile_fn(resolved)
            return True
        return False

    if sys.platform == "darwin":
        objc, _ = _load_macos_objc_and_gcd()
        msg_addr = ctypes.cast(objc.objc_msgSend, ctypes.c_void_p).value
        if not msg_addr:
            return False
        msg_id0 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(
            msg_addr
        )
        msg_id_cstr = ctypes.CFUNCTYPE(
            ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p
        )(msg_addr)
        msg_id_id = ctypes.CFUNCTYPE(
            ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
        )(msg_addr)
        msg_bool_id = ctypes.CFUNCTYPE(
            ctypes.c_byte, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
        )(msg_addr)

        cls_str = objc.objc_getClass(b"NSString")
        cls_url = objc.objc_getClass(b"NSURL")
        cls_ws = objc.objc_getClass(b"NSWorkspace")
        sel_str_utf8 = objc.sel_registerName(b"stringWithUTF8String:")
        sel_file_url = objc.sel_registerName(b"fileURLWithPath:")
        sel_shared_ws = objc.sel_registerName(b"sharedWorkspace")
        sel_open_url = objc.sel_registerName(b"openURL:")

        ns_s = msg_id_cstr(cls_str, sel_str_utf8, resolved.encode("utf-8"))
        ns_u = msg_id_id(cls_url, sel_file_url, ns_s) if ns_s else None
        ws = msg_id0(cls_ws, sel_shared_ws) if cls_ws else None
        if ws and ns_u:
            return bool(msg_bool_id(ws, sel_open_url, ns_u))
        return False

    return False


def _dispatch_files_to_plater(
    file_paths: Sequence[str | Path],
    timeout_ms: int = 5000,
) -> tuple[bool, str, int | None]:
    """Cross-platform in-process Plater file loader for Windows (`win32`) and macOS (`darwin`)."""
    if sys.platform == "win32":
        copydata_payload = _format_other_instance_payload(file_paths)
        hwnd = _find_orca_mainframe_hwnd()
        ok, msg = _dispatch_copydata_to_hwnd(
            hwnd or 0, copydata_payload, timeout_ms=timeout_ms
        )
        return (ok, msg, hwnd)

    if sys.platform == "darwin":
        ok, msg = _dispatch_macos_open_files(file_paths, timeout_ms=timeout_ms)
        return (ok, msg, None)

    ok, msg = send_linux_plater_request(_format_other_instance_payload(file_paths))
    return ok, msg, None


def _slugify_filename(name: str, fallback: str = "thread") -> str:
    """Slugify filename while scrubbing OrcaSlicer `PluginAuditManager` denied path keywords
    (`secret`, `cert`, `conf` — which C++ `is_denied_path_keyword` blocks case-insensitively).
    """
    cleaned = re.sub(r"[^\w\-. ]+", "", str(name or "").strip(), flags=re.ASCII)
    cleaned = re.sub(r"\s+", "_", cleaned).strip("._-")
    cleaned = re.sub(r"secret", "secr", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"cert", "crt", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"conf", "cfg", cleaned, flags=re.IGNORECASE)
    if not cleaned:
        return fallback
    return cleaned[:64]


def _extract_first_float(val: Any, default: float) -> float:
    if val is None:
        return default
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        f = float(val)
        return f if f == f else default
    if isinstance(val, (list, tuple)):
        for item in val:
            res = _extract_first_float(item, float("nan"))
            if res == res:
                return res
        return default
    s = str(val).strip()
    if not s:
        return default
    m = re.search(r"[-+]?\d*\.?\d+", s)
    if not m:
        return default
    try:
        return float(m.group(0))
    except ValueError:
        return default


def _parse_printable_area(
    raw: Any, default_x: float = 220.0, default_y: float = 220.0
) -> tuple[float, float]:
    """Parse OrcaSlicer `printable_area` into `(bed_x_mm, bed_y_mm)`."""
    if raw is None:
        return (default_x, default_y)

    xs: list[float] = []
    ys: list[float] = []

    tokens: list[Any]
    if isinstance(raw, str):
        s = raw.strip()
        if s.startswith("["):
            try:
                parsed = json.loads(s)
                tokens = parsed if isinstance(parsed, list) else [s]
            except Exception:
                tokens = re.split(r"[;,]+", s)
        else:
            tokens = re.split(r"[;,]+", s)
    elif isinstance(raw, (list, tuple)):
        tokens = list(raw)
    else:
        return (default_x, default_y)

    for tok in tokens:
        if isinstance(tok, (list, tuple)) and len(tok) >= 2:
            try:
                xs.append(float(tok[0]))
                ys.append(float(tok[1]))
            except (TypeError, ValueError):
                continue
        elif isinstance(tok, str):
            m = re.search(r"([-+]?\d*\.?\d+)\s*[xX:]\s*([-+]?\d*\.?\d+)", tok)
            if m:
                try:
                    xs.append(float(m.group(1)))
                    ys.append(float(m.group(2)))
                except ValueError:
                    continue

    if len(xs) >= 2 and len(ys) >= 2:
        dx = max(xs) - min(xs)
        dy = max(ys) - min(ys)
        if dx >= 30.0 and dy >= 30.0:
            return (round(dx, 2), round(dy, 2))

    return (default_x, default_y)


def _parse_line_width(raw: Any, nozzle_mm: float) -> float:
    default_lw = round(nozzle_mm * 1.05, 2)
    if raw is None:
        return default_lw
    if isinstance(raw, (list, tuple)):
        return _parse_line_width(raw[0] if raw else None, nozzle_mm)
    s = str(raw).strip()
    if not s:
        return default_lw
    if s.endswith("%"):
        pct = _extract_first_float(s[:-1], 0.0)
        if pct > 10.0:
            return round(max(0.2, min(2.5, nozzle_mm * (pct / 100.0))), 3)
        return default_lw
    val = _extract_first_float(s, 0.0)
    if val <= 0.05:
        return default_lw
    return round(max(0.2, min(2.5, val)), 3)


def _extract_preset_name(obj: Any, fallback: str = "") -> str:
    if obj is None:
        return fallback
    if isinstance(obj, str):
        return obj.strip() or fallback
    if isinstance(obj, dict):
        for k in ("name", "preset_name", "id"):
            v = obj.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
        return fallback
    for attr in ("name", "preset_name"):
        try:
            val = getattr(obj, attr, None)
            if callable(val):
                val = val()
            if isinstance(val, str) and val.strip():
                return val.strip()
        except Exception:
            continue
    return fallback


def _bundle_get_value(bundle: Any, key: str) -> Any:
    if bundle is None:
        return None
    for method_name in ("full_config_value", "config_value", "get"):
        fn = getattr(bundle, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "":
                    return val
            except Exception:
                continue
    return None


def _detect_language(app_info: dict[str, Any]) -> str:
    raw = app_info.get("language") or app_info.get("lang")
    if raw:
        return normalize_language(raw)
    try:
        return normalize_language(locale.getlocale()[0])
    except Exception:
        return "pt"


def _detect_theme(app_info: dict[str, Any]) -> str:
    theme_raw = (
        str(app_info.get("theme") or app_info.get("color_mode") or "").strip().lower()
    )
    if theme_raw == "light":
        return "light"
    if theme_raw == "dark":
        return "dark"
    if app_info.get("dark_mode") is False:
        return "light"
    return "dark"


def _make_execution_result_success(message: str) -> Any:
    exec_cls = getattr(orca, "ExecutionResult", None)
    if exec_cls is not None:
        success_fn = getattr(exec_cls, "success", None)
        if callable(success_fn):
            try:
                return success_fn(message)
            except TypeError:
                return success_fn(message, "")
        try:
            ok_code = getattr(getattr(orca, "PluginResult", None), "Success", 0)
            return exec_cls(ok_code, message, "")
        except Exception:
            pass
    return {"status": "Success", "message": message}


# ---------------------------------------------------------------------------
# Shared Thread Studio Session & Message Router
# ---------------------------------------------------------------------------


class ThreadStudioController:
    def __init__(self):
        self._lock = threading.RLock()
        self._current_params = normalize_params()
        self._listeners = []
        self._undo = []
        self._redo = []
        self._last_plater_worker = None
        self._last_plater_outcome = {}
        self._revision = 0
        self._worker_lock = threading.Lock()
        self._last_geometry_worker = None
        self._preferences_initialized = False
        self._client_requests = {}
        self._language_requests = {}
        self._language_revision = 0

    @property
    def current_params(self):
        with self._lock:
            return copy.deepcopy(self._current_params)

    def set_current_params(self, raw, history=True):
        p = normalize_params(raw)
        with self._lock:
            if p != self._current_params and history:
                self._undo.append(self._current_params)
                self._undo = self._undo[-50:]
                self._redo = []
            self._current_params = p
        return copy.deepcopy(p)

    def get_presets_dir(self):
        return _resolve_storage_dir() / "presets"

    def get_export_dir(self):
        d = _resolve_storage_dir() / "exports"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def read_host_context(self) -> dict[str, Any]:
        """Defensively inspect `orca.host.app_language()` and `orca.host.preset_bundle()`."""
        app_info: dict[str, Any] = {}
        host = getattr(orca, "host", None)
        if host is not None:
            # Official OrcaSlicer API Reference (`orca.host.app_language()`)
            app_lang_fn = getattr(host, "app_language", None)
            if callable(app_lang_fn):
                try:
                    raw_lang = app_lang_fn()
                    if isinstance(raw_lang, str) and raw_lang.strip():
                        app_info["language"] = raw_lang.strip()
                except Exception:
                    pass

            app_info_fn = getattr(host, "app_info", None)
            if callable(app_info_fn):
                try:
                    info = app_info_fn()
                    if isinstance(info, dict):
                        for k, v in info.items():
                            app_info.setdefault(k, v)
                except Exception:
                    pass

        lang = _detect_language(app_info)
        theme = _detect_theme(app_info)
        theme_explicit = bool(
            app_info.get("theme")
            or app_info.get("color_mode")
            or ("dark_mode" in app_info)
        )
        orca_version = str(app_info.get("version") or "2.5.1")

        bundle = None
        if host is not None:
            bundle_fn = getattr(host, "preset_bundle", None)
            if callable(bundle_fn):
                try:
                    bundle = bundle_fn()
                except Exception:
                    bundle = None

        printer_name = "Generic FDM 220x220"
        process_name = "0.20mm Standard"
        filament_name = "Generic PLA"

        if bundle is not None:
            for m in ("current_printer_preset",):
                fn = getattr(bundle, m, None)
                if callable(fn):
                    try:
                        printer_name = _extract_preset_name(fn(), printer_name)
                    except Exception:
                        pass

            for m in ("current_print_preset", "current_process_preset"):
                fn = getattr(bundle, m, None)
                if callable(fn):
                    try:
                        got = _extract_preset_name(fn(), "")
                        if got:
                            process_name = got
                            break
                    except Exception:
                        pass

            for m in ("current_filament_preset_names", "current_filament_presets"):
                fn = getattr(bundle, m, None)
                if callable(fn):
                    try:
                        fils = fn()
                        if isinstance(fils, (list, tuple)) and fils:
                            got = _extract_preset_name(fils[0], "")
                            if got:
                                filament_name = got
                                break
                    except Exception:
                        pass

            if printer_name == "Generic FDM 220x220":
                p_id = _bundle_get_value(bundle, "printer_settings_id")
                if isinstance(p_id, str) and p_id.strip():
                    printer_name = p_id.strip()

        bed_x, bed_y = _parse_printable_area(
            _bundle_get_value(bundle, "printable_area"),
            default_x=220.0,
            default_y=220.0,
        )
        max_z = max(
            50.0,
            min(
                1000.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "printable_height"), 250.0
                ),
            ),
        )
        nozzle_mm = max(
            0.15,
            min(
                2.0,
                _extract_first_float(_bundle_get_value(bundle, "nozzle_diameter"), 0.4),
            ),
        )
        layer_height_mm = max(
            0.04,
            min(
                1.2,
                _extract_first_float(_bundle_get_value(bundle, "layer_height"), 0.2),
            ),
        )
        line_width_mm = _parse_line_width(
            _bundle_get_value(bundle, "outer_wall_line_width"),
            nozzle_mm=nozzle_mm,
        )

        return {
            "lang": lang,
            "theme": theme,
            "theme_explicit": theme_explicit,
            "orca_version": orca_version,
            "printer_name": printer_name,
            "process_name": process_name,
            "filament_name": filament_name,
            "bed_x": float(bed_x),
            "bed_y": float(bed_y),
            "max_z": float(max_z),
            "nozzle_mm": float(nozzle_mm),
            "layer_height_mm": float(layer_height_mm),
            "line_width_mm": float(line_width_mm),
        }

    def read_full_host_config_snapshot(
        self, host_ctx: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Collect full resolved `project_settings` snapshot from `preset_bundle()` for `.3mf` export."""
        ctx = dict(host_ctx) if host_ctx is not None else self.read_host_context()
        project_settings: dict[str, Any] = {}

        host = getattr(orca, "host", None)
        bundle = None
        if host is not None:
            bundle_fn = getattr(host, "preset_bundle", None)
            if callable(bundle_fn):
                try:
                    bundle = bundle_fn()
                except Exception:
                    bundle = None

        if bundle is not None:
            keys_fn = getattr(bundle, "full_config_keys", None)
            val_fn = getattr(bundle, "full_config_value", None) or getattr(
                bundle, "config_value", None
            )
            if callable(keys_fn) and callable(val_fn):
                try:
                    keys = keys_fn()
                    if isinstance(keys, (list, tuple, set)):
                        for k in keys:
                            ks = str(k)
                            if not ks:
                                continue
                            try:
                                v = val_fn(ks)
                                if v is not None:
                                    project_settings[ks] = v
                            except Exception:
                                continue
                except Exception:
                    pass

        ctx["project_settings"] = project_settings
        return ctx

    def build_initial_context(self, mode="page"):
        host = self.read_host_context()
        if not self._preferences_initialized:
            try:
                saved = json.loads((_resolve_storage_dir() / "ui_preferences.json").read_text(encoding="utf8"))
                if isinstance(saved, dict) and isinstance(saved.get("lang"), str):
                    host = dict(host, lang=normalize_language(saved["lang"]))
            except (OSError, ValueError, UnicodeError):
                pass
            self.set_current_params(
                dict(self.current_params, lang=host["lang"], theme=host["theme"]),
                history=False,
            )
            self._preferences_initialized = True
        p = self.current_params
        return dict(
            params=p,
            host=host,
            mode=mode,
            builtin_presets=BUILTIN_PRESETS,
            user_presets=load_user_presets(self.get_presets_dir()),
            lang=p["lang"],
            theme=p["theme"],
        )

    def _geometry_message(self, params=None):
        p = normalize_params(params or self.current_params)
        parts = []
        warning = ""
        try:
            parts = collect_target_meshes(p)
        except ValueError as exc:
            warning = str(exc)
        theta = np.zeros(241)
        z = np.linspace(0, 2 * p["pitch"], 241)
        profile = dict(
            z=z.tolist(),
            male=thread_radius(theta, z, p).tolist(),
            female=thread_radius(theta, z, p, True).tolist(),
        )
        return dict(
            type="geometry",
            params=p,
            meshes=[
                dict(
                    name=name,
                    vertices=m.vertices.ravel().tolist(),
                    triangles=m.triangles.ravel().tolist(),
                    volume_cm3=m.volume_cm3,
                    bounds=m.bounds_mm,
                )
                for name, m in parts
            ],
            report=analyze_engagement(p),
            profile=profile,
            warning=warning,
            can_undo=bool(self._undo),
            can_redo=bool(self._redo),
        )

    def _reserve_client_request(self, message):
        """Under _lock, reject late deliveries from the same optional client."""
        client_id = message.get("client_id")
        request_id = message.get("request_id")
        if not isinstance(client_id, str) or not isinstance(request_id, int):
            return True  # Existing clients do not need correlation metadata.
        if request_id <= self._client_requests.get(client_id, -1):
            return False
        self._client_requests[client_id] = request_id
        return True

    def _commit_pending_edit(self, message):
        """Commit the toolbar's unsent edit in the same history transaction."""
        if "pending_params" not in message:
            return
        pending = message["pending_params"]
        if not isinstance(pending, dict):
            raise ValueError("pending_params must contain a parameter object")
        self.set_current_params(dict(pending, lang=self.current_params["lang"]))

    def _queue_geometry(self, request_id=None, client_id=None):
        with self._lock:
            if isinstance(client_id, str) and isinstance(request_id, int):
                if request_id < self._client_requests.get(client_id, -1):
                    return
                self._client_requests[client_id] = request_id
            self._revision += 1
            revision = self._revision
            p = self.current_params
            # The acknowledgement belongs to this exact parameter snapshot.
            acknowledgements = dict(self._client_requests)
        self._broadcast(dict(type="busy", busy=True))

        def generate():
            with self._worker_lock:
                with self._lock:
                    if revision != self._revision:
                        return
                try:
                    result = self._geometry_message(p)
                    with self._lock:
                        result["params"]["lang"] = self._current_params["lang"]
                    if request_id is not None:
                        result["request_id"] = request_id
                        result["client_id"] = client_id
                    result["client_acknowledgements"] = acknowledgements
                except Exception as exc:
                    with self._lock:
                        latest = revision == self._revision
                    if latest:
                        self._broadcast(
                            dict(
                                type="action_result",
                                ok=False,
                                paths=[],
                                message=str(exc),
                            )
                        )
                        self._broadcast(dict(type="busy", busy=False))
                    return
                with self._lock:
                    latest = revision == self._revision
                if latest:
                    self._broadcast(result)
                    self._broadcast(dict(type="busy", busy=False))

        self._last_geometry_worker = threading.Thread(target=generate, daemon=True)
        self._last_geometry_worker.start()

    def _broadcast(self, payload):
        for callback in self._listeners[:]:
            try:
                callback(payload)
            except Exception:
                self._listeners.remove(callback)

    def _write_exports(self, p, fmt):
        items = collect_target_meshes(p)
        base = self.get_export_dir() / (
            _slugify_filename(p["name"], fallback="thread") + "_" + uuid.uuid4().hex[:8]
        )
        if fmt == "3mf":
            return [
                str(
                    write_orca_3mf(
                        base.with_suffix(".3mf"),
                        items,
                        p,
                        self.read_full_host_config_snapshot(),
                    )
                )
            ]
        if fmt != "stl":
            raise ValueError("Unsupported export format")
        return [
            str(
                write_binary_stl(
                    base.with_name(base.name + "_" + name).with_suffix(".stl"), mesh
                )
            )
            for name, mesh in items
        ]

    def handle_message(self, raw_data, send_fn, default_mode="page"):
        try:
            msg = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
            if not isinstance(msg, dict):
                raise ValueError("Expected message object")
            action = msg.get("type", "")
            if action == "set_language":
                language = normalize_language(msg.get("lang"))
                client = msg.get("client_id")
                request = msg.get("language_request_id")
                with self._lock:
                    if isinstance(client, str) and type(request) is int:
                        if request <= self._language_requests.get(client, -1):
                            return
                        self._language_requests[client] = request
                    self._current_params["lang"] = language
                    self._preferences_initialized = True
                    self._language_revision += 1
                    revision = self._language_revision
                    directory = _resolve_storage_dir()
                    directory.mkdir(parents=True, exist_ok=True)
                    path = directory / "ui_preferences.json"
                    temp = directory / (".ui_preferences-" + uuid.uuid4().hex + ".tmp")
                    try:
                        temp.write_text(json.dumps({"lang": language}), encoding="utf8")
                        os.replace(temp, path)
                    finally:
                        temp.unlink(missing_ok=True)
                payload = dict(type="preferences_updated", lang=language,
                               language_revision=revision, language_request_id=request, client_id=client)
                self._broadcast(payload)
                if send_fn not in self._listeners:
                    send_fn(payload)
                return
            if action == "sync_printer":
                # Host refresh must not reset a design or queue new geometry.
                send_fn(dict(type="host_state", host=self.read_host_context()))
                return
            if action == "ready":
                if send_fn not in self._listeners:
                    self._listeners.append(send_fn)
                send_fn(
                    dict(
                        type="init_state",
                        request_id=msg.get("request_id"),
                        client_id=msg.get("client_id"),
                        **self.build_initial_context(default_mode),
                    )
                )
                self._queue_geometry(msg.get("request_id"), msg.get("client_id"))
                return
            if action in ("update", "analyze", "randomize", "reset"):
                with self._lock:
                    if not self._reserve_client_request(msg):
                        return
                    if action in ("randomize", "reset"):
                        self._commit_pending_edit(msg)
                    p = (
                        DEFAULT_PARAMS
                        if action == "reset"
                        else msg.get("params", self.current_params)
                    )
                    if action == "randomize":
                        p = generate_random_printable_params(msg.get("seed"), p)
                    p = dict(p, lang=self._current_params["lang"])
                    self.set_current_params(p)
                self._queue_geometry(msg.get("request_id"), msg.get("client_id"))
                return
            if action in ("undo", "redo"):
                with self._lock:
                    if not self._reserve_client_request(msg):
                        return
                    self._commit_pending_edit(msg)
                    source, target = (
                        (self._undo, self._redo)
                        if action == "undo"
                        else (self._redo, self._undo)
                    )
                    if source:
                        target.append(self._current_params)
                        language = self._current_params["lang"]
                        self._current_params = dict(source.pop(), lang=language)
                self._queue_geometry(msg.get("request_id"), msg.get("client_id"))
                return
            if action == "preset_save":
                data = save_user_preset(
                    self.get_presets_dir(),
                    msg.get("name", "Preset"),
                    msg.get("params", self.current_params),
                    msg.get("id"),
                )
                self._broadcast(dict(type="presets_updated", user_presets=data))
                return
            if action == "preset_delete":
                data = delete_user_preset(self.get_presets_dir(), msg.get("id", ""))
                self._broadcast(dict(type="presets_updated", user_presets=data))
                return
            if action in ("export_file", "send_to_plater"):
                with self._lock:
                    p = self.set_current_params(dict(msg.get("params", self.current_params), lang=self._current_params["lang"]))
                fmt = msg.get("format", "3mf")
                send_fn(
                    dict(
                        type="action_result",
                        ok=None,
                        action=action,
                        paths=[],
                        message="Preparing mesh…",
                    )
                )

                def export_worker():
                    try:
                        paths = self._write_exports(p, fmt)
                        if action == "export_file":
                            result = dict(
                                type="action_result",
                                ok=True,
                                action=action,
                                paths=paths,
                                message="Files exported.",
                            )
                        else:
                            ok, detail, hwnd = _dispatch_files_to_plater(paths)
                            result = dict(
                                type="action_result",
                                ok=ok,
                                action=action,
                                paths=paths,
                                message=("Import request sent; loading not confirmed." if ok else "Transport failed."),
                                detail=detail,
                            )
                    except Exception as exc:
                        result = dict(
                            type="action_result",
                            ok=False,
                            action=action,
                            paths=[],
                            message=str(exc),
                        )
                    self._last_plater_outcome = result
                    send_fn(result)

                self._last_plater_worker = threading.Thread(
                    target=export_worker, daemon=True
                )
                self._last_plater_worker.start()
                return
            if action == "open_exports":
                ok = _open_folder_native(self.get_export_dir())
                send_fn(
                    dict(
                        type="action_result",
                        ok=ok,
                        paths=[str(self.get_export_dir())],
                        message="Open export folder",
                    )
                )
                return
            raise ValueError("Unknown command: " + str(action))
        except Exception as exc:
            send_fn(dict(type="action_result", ok=False, paths=[], message=str(exc)))


_SHARED_CONTROLLER = ThreadStudioController()


class ThreadStudioPageCapability(orca.pages.PagesPluginCapabilityBase):
    """Full-screen top-bar tab (`Thread Studio`) beside Prepare / Preview / Device."""

    def __init__(self, controller: ThreadStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Thread Studio"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "default_module": "container_and_lid",
            "default_standard": "fdm_trapezoid_45",
            "default_export_target": "all",
            "auto_configure_slicer": True,
        }

    def get_icon(self) -> str:
        storage_dir = _resolve_storage_dir()
        existing_candidates: list[Path] = []
        try:
            existing_candidates.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        existing_candidates.extend(
            [
                storage_dir / "icon.svg",
                _default_installed_plugin_dir() / "icon.svg",
            ]
        )
        for cand in existing_candidates:
            try:
                if cand.is_file() and cand.stat().st_size > 0:
                    return str(cand)
            except Exception:
                continue

        # Auto-materialize embedded `icon.svg` when user side-loaded only `orca_thread_generator.py`
        write_targets: list[Path] = [
            storage_dir / "icon.svg",
            _default_plugin_data_dir() / "icon.svg",
        ]
        try:
            write_targets.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        write_targets.append(
            Path.home() / "Documents" / "OrcaThreadStudio" / "icon.svg"
        )

        seen_dirs: set[str] = set()
        for target in write_targets:
            key = str(target)
            if key in seen_dirs:
                continue
            seen_dirs.add(key)
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                with open(target, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(ICON_SVG_CONTENT)
                if target.is_file() and target.stat().st_size > 0:
                    return str(target)
            except Exception:
                continue
        return ""

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="page")
        return get_studio_html(mode="page", initial_context=initial_ctx)

    def post_message(self, data: Any) -> None:
        super_post = getattr(super(), "post_message", None)
        if callable(super_post):
            super_post(data)

    def on_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self.post_message,
            default_mode="page",
        )


class ThreadStudioDockCapability(orca.script.ScriptPluginCapabilityBase):
    """Opens/shows a docked right-hand Thread Studio panel directly beside the 3D Plater."""

    _active_panel: Any = None
    _panel_lock = threading.RLock()

    def __init__(self, controller: ThreadStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Orca Thread Studio - Painel Lateral"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "default_export_target": "all",
            "auto_configure_slicer": True,
            "dock_side": "right",
        }

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="dock")
        return get_studio_html(mode="dock", initial_context=initial_ctx)

    def _post_to_panel(self, payload: dict[str, Any]) -> None:
        with self._panel_lock:
            panel = ThreadStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            is_open_fn = getattr(panel, "is_open", None)
            if callable(is_open_fn) and not is_open_fn():
                return
            post_fn = getattr(panel, "post", None)
            if callable(post_fn):
                post_fn(payload)
        except Exception:
            pass

    def _on_panel_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self._post_to_panel,
            default_mode="dock",
        )

    def _on_panel_close(self) -> None:
        with self._panel_lock:
            ThreadStudioDockCapability._active_panel = None

    def on_message(self, data: Any) -> None:
        """Direct message entry point for testing or programmatic invocation."""
        self._on_panel_message(data)

    def execute(self) -> Any:
        """Invoked on OrcaSlicer's background Script worker thread."""
        with self._panel_lock:
            existing = ThreadStudioDockCapability._active_panel

        if existing is not None:
            try:
                is_open_fn = getattr(existing, "is_open", None)
                if not callable(is_open_fn) or is_open_fn():
                    show_fn = getattr(existing, "show", None)
                    if callable(show_fn):
                        show_fn()
                    init_ctx = self._controller.build_initial_context(mode="dock")
                    self._post_to_panel({"type": "init_state", **init_ctx})
                    return _make_execution_result_success(
                        "Painel lateral Orca Thread Studio exibido."
                    )
            except Exception:
                with self._panel_lock:
                    ThreadStudioDockCapability._active_panel = None

        html = self.get_ui()
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        create_dock_fn = (
            getattr(ui, "create_dock_panel", None) if ui is not None else None
        )

        if callable(create_dock_fn):
            panel = create_dock_fn(
                html,
                title="Orca Thread Studio",
                width=430,
                height=800,
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
                dock="right",
            )
            with self._panel_lock:
                ThreadStudioDockCapability._active_panel = panel
            if panel is not None:
                show_fn = getattr(panel, "show", None)
                if callable(show_fn):
                    try:
                        show_fn()
                    except Exception:
                        pass
            return _make_execution_result_success(
                "Painel lateral Orca Thread Studio aberto."
            )

        create_win_fn = getattr(ui, "create_window", None) if ui is not None else None
        if callable(create_win_fn):
            panel = create_win_fn(
                html,
                title="Orca Thread Studio",
                width=450,
                height=820,
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
            )
            with self._panel_lock:
                ThreadStudioDockCapability._active_panel = panel
            return _make_execution_result_success("Janela Orca Thread Studio aberta.")

        return orca.ExecutionResult.failure(
            orca.PluginResult.RecoverableError,
            "This host does not provide a dock or window API",
        )


# ---------------------------------------------------------------------------
# Single `@orca.plugin` Entry Point Class
# ---------------------------------------------------------------------------


@orca.plugin
class OrcaThreadStudioPlugin(orca.base):
    """OrcaSlicer 2.5.1+ Native Plugin Entry Point for Orca Thread Studio."""

    def __init__(self) -> None:
        super().__init__()

    def register_capabilities(self) -> None:
        """Declare required plugin permissions and register Page + Script Dock capabilities.

        Per OrcaSlicer's `Plugin Audit Hook` specification:
        - `data_dir()` (`orca_plugins` and `orca.host.plugin.storage()`) is already a global
          read+write Allowed Root requiring zero `fs_read`/`fs_readwrite` prompts.
        - `has_permission` uses exact string equality (glob wildcards like `/*` are invalid).
        - `threading=True` declares the fixed `"thread"` audit target once up front.
        """
        req_fn = getattr(orca, "request_permissions", None)
        if callable(req_fn):
            req_fn(threading=True)

        orca.register_capability(ThreadStudioPageCapability)
        orca.register_capability(ThreadStudioDockCapability)
