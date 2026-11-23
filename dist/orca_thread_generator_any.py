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
