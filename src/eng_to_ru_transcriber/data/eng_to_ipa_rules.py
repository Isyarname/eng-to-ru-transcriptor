
macros = {
	"_V": "[aeiouy]",
	"_C":"[bcdfghjklmnpqrstvwxz]",
	"i?": "(i|)",
    "!ʲ": "(?!ʲ)",
    "_":""

}



rules = '''

j -> dʒ
_Vh$ -> _V


[ABCDEFGHIJKLMNOPQRSTUVWXYZ] -> (ej|biː|siː|diː|iː|ef|dʒiː|ejtʃ|aj|dʒej|kej|el|em|en|oʊ|piː|kjuː|ɑː|es|tiː|juː|viː|dʌbəljuː|eks|waj|zed)

y[aeiou] -> j[aeiou]
ti[oa]n$ -> ʃən
_Vsion -> _Vʒən
_Csion -> _Cʃən
[tc]ial$ -> ʃəl
ture$ -> tʃə
tech -> tek
core$ -> kɔː
[tc]ious -> ʃəs
micro -> majkro
^pre -> prɪ
^_C_C?ies$ -> _C_C?ajz
ies$ -> iz
^_C_C?ied$ -> _C_C?ajd
ied$ -> id
igh->aj
gh->g
(c|ch|sh|x|z)es$ -> (c|ch|sh|x|z)ɪz
(t|d)ed$ -> (t|d)ɪd
ly$ -> lɪ
qu -> kw
^x_V -> z_V
_Vx_V->_Vgz_V
x -> ks
sch -> sk
sc[eiy] -> s[eiy]
t?ch -> tʃ
sh -> ʃ
th -> θ
ph -> f
c[eiy] -> s[eiy]
are -> eə
[oeiu]re -> (ɔː|ɪ|aj|jʊ)ə
[aeiouy]r!V -> (ɑː|ɜː|ɜː|ɔː|ɜː|ɜː)
all -> ɔːl
alk -> ɔːk
alm -> ɑːm
a[uw] -> ɔː
wa -> wɒ
[eo]a_C -> (iː|oʊ)_C
ai_C -> ej_C
ou_C -> aʊ_C
oi_C -> ɔj_C
ook -> ʊk
oo -> uː
ee -> iː
oe -> uː


ie -> iː
old -> oʊld
ind -> ajnd
[ao]y -> [eɔ]j
_Vy_C -> _Vj_C
[aio]_C_V -> (ej|aj|oʊ)_C_V
u_C_e -> juː_C_e
(ej|aj|oʊ|juː)_Ce -> (ej|aj|oʊ|juː)_C
_Ces$ -> _Cɪs$
_Ced$ -> _Cɪd$
[aeiou]_C!_V -> [æeɪɒʌ]_C
[vs]e[sd]?$ -> [vs][sd]?$
(æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː|ʊ)s(æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː|l) -> (æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː|ʊ)z(æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː|l)
_Cy_C -> _Cɪ_C
e[wu] -> juː
n[gk] -> ŋ[gk]
kn -> n
gn -> n
mb -> m
c -> k
r -> ɹ
y$ -> ɪ
[ptkfsθʃ]s$ -> [ptkfsθʃ]s
(b|d|g|v|ð|z|ʒ|m|n|ŋ|l|r|w|aj|æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː)s$ -> (b|d|g|v|ð|z|ʒ|m|n|ŋ|l|r|w|aj|æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː)z
[ptkfsθʃ]ed$ -> [ptkfsθʃ]t
(b|d|g|v|ð|z|ʒ|m|n|ŋ|l|r|w|aj|æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː)ed$ -> (b|d|g|v|ð|z|ʒ|m|n|ŋ|l|r|w|aj|æ|e|ɪ|ɒ|ʌ|uː|iː|eə|ɔː|ɜː|ɑː)d
_C{2} -> _C

'''