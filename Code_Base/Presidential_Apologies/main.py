import re

# file = open("../Sources/English/English Presidenial Apology.txt", "r")
# t  = file.read()
# print(len(t.split(".")))

# file = open("../Sources/Chinese/Traditional Chinese Presidential Apology.txt", "r")
# p  = file.read()
# p = p.split("。")
# # print(len(p.split("。")))
# print(len(p))
# print(p[98:])

# file = open("../Sources/English/test.txt", "r")
# t  = file.read()
# t = t.split('.')
# print(len(t))
# print(t[98:])
# for i in range(len(p)):
#     print(p[i], f" \n {i} ----------- \n")

# file = open("../Sources/English/test2.txt", "r")
# t  = file.read()
# t = t.split('.')
# t=t[:-1]
# print(len(t))


# file = open("../Sources/English/test3.txt", "r")
# p  = file.read()
# p = p.split('。')
# p = p[:-1]
# print(len(p))



# for i in range(101):
#     print(t[i], "\n", p[i])
#     print(f"{i}\n--------------\n")


t = """
to nia auyusi no tompuska ueso. ‘o senfa(憲法) isi sopuhngi hocu teovahi ne ohec’ola yainca 「yata fuengu」‘e cou ta taivang hocu poa 「anana’o yatan’e ci cou」,’emo maica totuhci ta ongko, o’a isi anova saapayo’a na noana’o cimo yaa potfngʉ ci pat’auna. isin’a epopayoa ho zou atuhcu yata taivang ‘e suezop no cou. 
i’tohungu tan’e. teto toehungu m’esuhcu maitan’e. te’o yac’ʉ ta ateunu ‘oyona tmopsʉ maitan’e, boemi no mʉ’eona ta ‘tohʉngʉ ho mi’usnu ta acʉcʉhʉ ci suezopʉ no cou ta taivang ho eovei. ina ohola miya ci tose’sʉpta ci hie. mimu smovei no ma’tutumzo ho ‘oha ahmxskʉ cila ti’a’ausna, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu muu ho eovei. 
os’o taa’uzva(taa’uiva), ac’ʉhʉ maitan’e, ta aukukuyungu ta h’oyunsovato, mioc’on’a yaa maica ci ‘tohʉngʉ o’ante ‘ahʉyʉ eovei. ‘aeno na eni, na te’o koa asuhcu yac’ʉ ta ateunu ‘oyona tmopsʉ ho eovei. lahe yainca no koyuhe, ‘o niala ‘oha ahmʉskʉ hocieno na nia ‘atutumzo to mocmo ci suezopʉ ‘alaeno anana’va esmiza(esmia) hote yusuhci ‘e yatatiskova. na eni temza yac’ʉ tan’e, ta’koeva no aezuha ho taiezuha ‘emo maica ci hia ma’to’tohʉngʉ. 
te’o titho tate ta’hongi ci e’e ho pateafa na koa mi’usnu ta suezopʉ no cou ta taivang ho eovei. ‘e ceoa ta taivang, auyusi no tose’sʉpta mohcula yaa nouyu ci yatatiskova. ‘emo maica ci yatatiskova mosola anana’o yaa iachi h’oyunsova, yaa iachi h’oe’eya, h’oceoceona, at’oca ci hupa. acnguhu, moso yono o’amoso yupa tohmʉskʉ ci ‘tohʉngʉ, moso esmi ta ceoa tan’e ‘omo h’uasi ci suezopʉ, to a’a’ausna ne auyusi, ‘emo uafeihi ci cou ohecu ti’einga ‘e acʉcʉhʉ ta moso nouyu ci cou. poa meaapapayo’ʉ ta ohela atva’esa at’oca ci ceoa. nama micuc’o mais’a yano yafana. o’a na atuhcusi ho cuc’o poasaskita ci cou. 
hola meelʉ biʉlʉlʉ emo coni ci suezopʉ, asonʉ na’nosi p’eac’a no ‘atutumio no mocmo ci suezopʉ, mac’oci o’te ‘ahʉyʉ iachi mainca zou moulʉlʉ ci hpʉhpʉngʉ, o’ate peelʉi o’te mipo’ʉ’ʉmti ho esansana na nia a’ʉmtʉsi ne auyusi, ataveisi, nate sotva’esa, ‘e ;oyonatmopsx te asansano nomio no niala auyusi ho yaa mou’ʉmtʉ ci ma’vovei, ‘aeno eni na koa’u yac’ʉ tan’e maitan’e. 
panto conci tposʉ isi yainca[tposx no auyusi ta taivang], isi engha to ehoisi ho yainca:[ uk’a ci nia auyusi ta taivang. ohe paavi to ‘olan( 荷 蘭 ), hioa to teizi( 鄭 氏 ), yaezoya to seizi( 清 朝 ).] ‘aeno eni na lahe hia baito no nia auyusi ta taivang to puutu. ‘e suezopʉ no cou, auyusi no toposifou, mohcula ‘auesiesi yayo ta ceoa tan’e, mo iachi yaa atngaso ci h’oceoceona ho moutʉs’ʉ, ho yu’ticngicngiha. at’inghi lac’o i’mi no bitaso ci hia baito ho tposi ‘e nia auyusi, nomio tan’e, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu ta suezopʉ no cou ho eovei. 
‘oniaseizi( 治 理 )to‘olan( 荷 蘭 )hoteisekoo ( 鄭 成 功 )ohe ake’a potpapayo’a ‘o suezopʉ to peepoa( 平埔 ) ho pa’mamaesih’a na ohela noe’oci no h’oyunsovahe, na nia meoino yu’tihmuhmuyu ho pohcingha to mansei( 滿 清 ), ho ine ohecula aʉt’ʉca to maaya ho ohmʉs’onʉ ta cou ho yainca te tasucza ci seisaku( 政策 ), ac’ʉhʉ ne ohecu tiuska ta puutu ne apihana ‘e hxpxhxpxxngx, ho ‘ahʉhʉya poa bua puutu ‘e cou ta ‘ayumonasi ta tose’sʉpta, cono hola esmi ‘emo cono suezopʉ, la boepapak’i ho pohcinghi, tophuhcu ta ceoa, a’ʉmta kuici akuzkuzoa ‘e mosola anana’o yayo ci kenli( 權利 ), nomio tan’e, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu ta suezopʉ no cou ho eovei. 
				
‘e suezopʉ no cou la fiho to iachi h’oceoceona ho ko’ko tmuteuyunu ‘e cono hosa, a’vinano fiho to moutʉs’ʉ ci h’oceoceona ho meelʉ e’tatiski na maunsonsou ta ‘oyona. at’inghi, yonta ‘ayumona ho isi seolʉa no p’eyac’a ‘emo faeva ci hpʉhpʉngʉ, isi payo’a ta suezopʉ no cou na kenli( 權利 ) no iyachi esvʉtʉ ho iyachi aʉt’ʉcʉ. micu aemo’ʉ na niala t’ʉcna no tmuteuyunu, o’anala tiova ta meoino hʉpʉhpʉʉngʉ na ohola toehunga tae’oci. nomio tan’e, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu ta suezopʉ ta cou ho eovei. 
‘e suezopʉ no cou mosola iyachi yaa h’oe’eya, nocaefi to maaya ho ohela aʉt’ʉca ho ocia poa tmumaaya, ho ine ataveisi no moso 1945, ohela potani ta seifu ‘e cou hocin’a buacou, cu i’mizi no meoino aapayo’ʉ ‘e iyachi h’oe’ea. aavaho i’o ohola yainca peepoa( 平埔 ) ci suezopʉ, micu a’ʉmta aʉlʉ aapapayo’ʉ ‘o nia e’ehe. ‘omosola afu’u aʉt’ ʉcʉ ne auyusi, o’a ohola peispo’ʉ’ʉmti na poa tʉyʉcneni na h’oceoceona ta suezopʉ no cou. nomio tan’e, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu ta suezopʉ ta cou ho eovei. 
ne mihnan’a, yono o’a ihe cohivi ci a’a’ausna to suezopʉ to taa’u( 達悟 ), ‘e seifu ohe soʉlʉlʉa to lahe yoni ci ceoa ‘o caciha no mahiz’o(mahi’o) ci pucu, poa svieni ta suezopʉ to taa’u na ma’sasmoyo no mahiz’o, nomio tan’e, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu ta suezopʉ to taa’u( 達悟 ) ho eovei.						
ahoi ho mohcu yʉmeʉmʉ ta taivang ‘o yane yafana, i’o mosola yonta maoponeo ta meoveana ci suezopʉ no peepoa( 平 埔 ) oho atva’esa aueva noa potpapayo’a. ohela aʉt’ʉca ho aapayo’a na ongko nohe cono suezopʉ, nomio tan’e, to taa’u( 達悟 ) ho mi’usnu ta suezopʉ ta peepoa( 平埔 ) ho eovei. 
ne mohcu tmai’usu no minsiu( 民 主 ) ‘e hpʉhpʉngʉ, ohela i’nanʉska yut’inga ta oyona tmopsʉ, mosola maezo i’nanʉskʉ pano ohela hi’hioa, maitan’e panto isi ake’a husuhca ci hoolicu no《原住民族基本法》, at’inghi ‘e hoolicu eni, ma’i ihe a’ʉmta angaboa huecvʉha tala yaahioa ta ‘oyona tmopsʉ, lamia ‘oha peismonʉ’ʉ, o’te amsoa peisngaboi, o’te amsoa poulʉlʉa. nomio tan’e, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu ta suezopʉ ta cou ho eovei. 
la yainca zou meoi no hʉpʉhpʉʉngʉ no atvohʉ ci h’oceoceo ‘e taivang. at’inghi ac’ʉhʉ maitan’e, na yoayokeo, ma’cohio, h’oyunsova no keizai( 經 濟 ), peis’upu no seizi( 政 治 ), mioc’on’a asngʉcʉ askucuhe ta o’a suezopʉ no cou. a’vinano ‘o anana’o potfʉnga ci hiahe baito ta suezopʉ no cou. o’amo ahtu aapayo’ʉ. o’amo amso man’i nala hioa ta ‘oyona tmopsʉ, poa tiou no o’a ohela esmiza to mocmo ci suezopʉ ci ma’tutumzo, nomio tan’e, te’o yac’ʉ ta ateunu ‘oyona tmopsʉ ho mi’usnu ta suezopʉ ta cou ho eovei. 
o’a mimza amso butotaso, a’vinano aucngicngihi o’te osnia husansana ho o’amimza butotaso, ko’koeno ac’ʉhʉ maitan’e ho poa elʉa no ‘atutumzo ‘e feangomu. a’ʉmtʉs’a pa’hikokoe’i. ‘e eovei maitan’e, e’vono micu na’no poha’o, at’inghi te yainca zou ahoisi. o’a os’o yainca tesiscus’a aususeoma ta moc’o matnʉskʉ ci tposʉ no eovei na nia alolongʉ no tose’sʉpta. at’inghi te’o i’mʉs’oneni ta ‘tohʉng’u ho mingeovi, ‘e eovei maitan’e, zou ahoisi no emo’usnu no nananghingiya ‘e ‘ayumona tamo cono hpʉhpʉngʉ. 
					
teomneni te’o boemi ta moutʉs’ʉ no suezopʉ no cou ho esansana ‘e hia noteuyunu maitan’e. to e’e to taiyalu ‘o [a’ʉmtʉsi] la yainca balay. ‘o [eususeomʉ] la yainca sbalay. ‘e auyusi ta balay isi sopuhngi ta S. ‘e [a’ʉmtʉsi] ho [eususeomʉ] mo natʉ’ca ci hia ma’to’tohʉngʉ, pateivha, na a’ʉmtʉ no eusʉseomʉ, te i’mi no mipo’ʉ’ʉmti na a’ʉmtʉsi niante peelʉi peihcʉ’hi. 
to h’oceoceona ta suezopʉ no cou, ‘e cono hosa, hoci yaa ‘oha einu ho elolongʉ no mocmo, hoci mainca no koyu te mici eususeomʉ, ‘o mamameoi lahe eteuyuna ‘omo akuzkuzo ho i’o isi akuzkuzoa, poa noepohʉ aʉlʉ yupa mi’usnu ho eʉsvʉta na nia a’ʉmtʉ ‘tohʉngʉ, ataveisi ho isucu esansana na ‘tohʉngʉ, tena toehungu pesonʉ tomo cono soetohvʉ ci emi, poacu sucaefi ‘e mohcu nocaefi ci hi’hioa, ‘aeno eni na isi yainca [sbalay]. 
te’o totea ‘e hioa maitan’e, ‘aeno te meelʉ [sbalay] ‘e ‘oyona tmopsʉ ho i’e suezopx no cou. pnanfi na tonʉ ho esansana na niala peis’epo, na nia a’ʉmtʉsi, uk’a eyava ho esansana. ho aomane, ‘o nanghia’u ta suezopʉ no cou tesi yaeza eh’ʉta na ‘tohʉngʉsi. o’ate’o smeecʉ’ho m’ea peu’uzva maitan’e, at’inghi te’o tata’ia temu ma’eʉyʉcʉ ho mingeovi, na niala peis’epo ne noana’o o’anate i’vaha peisvahi, ‘e hpʉhpʉngʉ eni, tenala yaa hiesi, meelʉ 					
a’ʉmtʉ emo’usnu no eususeomʉ. ‘e maitan’e tec’on’a yainca ahoisi, nate smovei no eususeomʉ o’ate tomakneni ta suezopʉ no cou hocieno feango to suezopʉ to peepoa( 平 埔 ), mante yonta ‘oyonatmopsʉ. os’o cohivi, hocic’o ngayoc’o na eususeomʉ o’ate ahtu amso, acʉhʉ cite hioaneni ta suezopʉ no cou, zou t’ʉcna no a’ʉmtʉ eususeomʉ ta hpʉhpʉngʉto. 				
te’o yontan’e hocu a’ʉmta epeaska, ‘e sotokufu( 總統府 ) te m’eyac’ʉ to [moulʉlʉ ci lekisi ho tmai’usnu no moulʉlʉ ci ‘i‘in kai ( 委 員 會 )]. te’o ieni ta ongkono’u tmuoteuyuna ta hpʉhpʉngʉ, iachia hioa na tela euteuyunu, toehungu na taihio to masusuezopʉ ho i’ima na moso moulʉlʉ ci nia aoyusi, maezo e’hahmʉskʉ toehunga tousvʉsvʉtʉ no tenala emo’ausna ta hpʉhpʉngʉ tan’e.
te’o ep’opnanfa, ina ‘i’ingkai ( 委 員 會 ) ta sootukufu( 總 統 府 ), nate atva’esa huecvʉha te e’hahmʉskʉ na natʉ’ca ta hpʉhpʉngʉ ho i’e suezopʉ no cou. nate hia m’eac’ʉ ta taihio ta masusuezopʉ, ta’upa ‘o suezopʉ to peepoa 平 埔 , te acʉhʉ i’tohungu no tohmʉskʉ na suezopʉ ho ina hosa, ‘e totnguca eni tena toehungu mooyai ‘oesvʉtʉ ta suezopʉ no cou, peelʉi a’ʉmta psoecʉ’ha eʉsvʉta na ‘tohʉngʉ ta cono suezopʉ. 
i‘omon’a h’unasi, te’o m’ea poa asvʉtʉ no hie ‘e 行政院 ho toʉsvʉsvʉtneni ‘o 「原住民族基本 法推動會」. na tela esvʉta ci seisaku ( 政策 ) ta ‘i’inkai 委員會 . no ataveisi ta ‘oyona tmopsʉ, tenoc’ʉhʉta 行政院,yu’tasvʉtʉhotasucza namo natʉ’ca ci hioa. ‘ete hi’hioa ta ‘ayumonasi te yosu’ka na isin’a talʉa ci lekisi、poot’ova ‘o iachi aʉt’ʉcʉ ta suezopʉ no cou、ahmʉskʉ ci posuhcu no keizai 經 濟、hona hia ma’cohio ho ina yu’ticngihi no h’oceoceona、aʉt’ʉca na yoayokeo ci feango, ho i’o noʉt’ʉ ci na kenli 權 利 tamo yonta hosa ta ngeesangsi ci suezopʉ no cou. 
e’unu ta hoolicu( 法 律 ) maitan’e ho ina ‘auesiesi ceoceona ta suezopʉ no cou, panto mo ‘oha yupa toseolʉ, teto m’eac’ʉ note a’sʉftonʉ ma’pongpangnʉ’ʉ ci 「 原 住 民 族 法律服務中心」, ieni note suce ci h’oesvʉta ho poa ma’susuce nala yupa poohcʉvho ‘e isi at’oca ci h’oceoceona no cou ho i’e esvʉta ta hoolicu 法律 maitan’e. 
temia poucufna namo yupa natʉ’ca cila yaahioa, osnia hioa ho tasucza, namo nomio no h’oceoceona ho yonta ‘ausiesi hupa, hoci o’amo nomio no ‘amamhimhino, o’amo mayo to isi afnasa aʉt’ʉca ci yuansou ho noa ehpʉngneni ne hooin 法 院 ho i’o isi yʉsvʉta no poekotva, mituhci ‘emo maica ci hi’hioa, te toehunga tousvʉsvʉneni nate ti’a’ausna. 
te’o yaeza poucufna namo yupa natʉ’ca yaahioa ta seifu, mituhci ‘o 核 廢 料 ho isi sia ne lanyi 蘭 嶼 , pahsansana namo yupa natʉ’ca ci niala esvʉtʉ. ho o’amocu te cohivi nate sotaveisi note soʉlʉlʉi, te fii note ‘aseolʉ ci tmuhnoa ‘e cou ta yamei 雅美 . 					
conosi hie, yono einva ‘o suezopʉ to pepoa 平 埔 homo iachi ma’cacou, esansana na iachihe ongko, auyusi no feohno ’siya, temia toʉsvʉsvʉtneni namo yupa natʉ’ca ci hoolicu 法 律 , poa esvovei na anana’ohe ongko ho inantehe anana’va tʉyʉca ci kenli 權利 . 
hotena feohʉ no maskʉ veia ucni,tenamiacu ahoza ta’koeva ho epeska na ceoa no ‘auesiesi hupa ta suezopʉ no cou, ‘o 部 落 公法人的制度 ,imizacu poot’ova hocu hioa, ho aomane tec’u macoconi hioa ‘o ohola ta’koeva ci iachi axt’ʉcʉ ‘e suezopʉ no cou, temia toupupcio ho aupcieva pa’i’usna nelipoin 立 法 院‘ohoolicu 法 律noiachi aʉt’ʉcʉ, hoolicu 法律 no ceoa ho hoolicu no etʉpʉ, hoolicu no ec’ʉvi ‘e e’e ta suezopʉ no cou, ho ataveisi no cohzona maitan’e temia hioa na toʉsvʉsvʉtʉ no esansana nate 
seisaku 政策 ta suezopʉ no cou. ataveisi to feohno’voeva tela aacnia mi’uneni ta yatatiskova ta cono hpʉhpʉngʉ ho eʉsvʉta na isicu peihcʉ’hi no moulʉlʉ ci lekisi ho ina tmai’usnu moulʉlʉ, a’ʉmta poa tmaʉlʉlʉ na moulʉlʉ ci lekisi, a’vinano p’eyac’a na tesi tnguci no iachi aʉt’ʉcʉ ‘e suezopʉ no cou, ‘aeno ‘emo tuyu nate mituhci no seisaku ta ‘oyona tmopsʉ. 
te’o eho’a ‘emo yontan’e, ho inamo baito no televi ho inamo buhmi no kanpiuto ci suezopʉ no cou, teto toehunga huomia. te’o eho’a na maananghia ho toehunga pocenga, o’ate yainca te epici. te’o noa sothi, pahsʉsʉfti, poa meelʉ peihcʉ’ho no ohola afu’a esvʉta ci hioa ‘e ‘oyona tmopsx, a’ʉmta teovahi na mosola o’te emzo no auyusi. 
te’o to’aveoveoyʉ ta acʉcʉhʉ ci nanghia ta suezopʉ no cou, zou muu na mimu e’sasmome ta afu’u yata hpʉhpʉngʉ tan’e, ‘e isi p’ecihi ci ceoa, ho i’emo noana’o ci h’oceoceona, yayo na o’ate peelʉi peʉezi ci huphina. ‘emo maica ci huphina, nate fii no so’einva. 
ho aomane, temia ieni ta poot’ou no seisaku 政 策 , nate ticngihi cite yutotavei, aucngucnguhu ci suezopʉ, ho i’emo yonta ceoa ta taivan ci suezopʉ, poa o’tena payo’ʉ no e’e, poa o’te ma’payo’ʉ ‘e ‘tohʉngʉ, afnaso o’te yupa namcovha ‘e iachi h’oceoceona, o’a nate i’vaho meaavovei ta iachi ceoa. 
te’o noa toehungu bitotonʉ ‘e aucunu ci hpʉhpʉʉngʉ, honga ‘e iachito auyusi, honga ‘e ceoato, yaeza honga na h’oceoceona tamo mav’ov’o ci suezopʉ. emo’usnu no yupa naovei, emo’usnu no tmucni ho toehungu psoevohngʉ, emo’usnu note faeva ci taivan no ataveisi. 
te’o m’ene ta acʉcʉhʉ ci ‘oahngʉ ta cono hpʉhpʉngʉ, ieni tamo ‘oc’ocic’o ci hie maitan’e, toehungu bitotonʉ ho m’eac’ʉ no conci moulʉlʉ ci hpʉhpʉngʉ, coni cimo ahmʉskʉ ho ‘enepio no suezopʉ ci hpʉhpʉngʉ.					
‘aveoveoyʉ. yokeoasu.
"""

print(len(t.split('.')))