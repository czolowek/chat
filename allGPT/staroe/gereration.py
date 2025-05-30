import os

# Путь к существующей папке "allGPT"
folder_path = "allGPT"

# Проверяем, что папка существует
if not os.path.exists(folder_path):
    raise Exception(f"Папка '{folder_path}' не найдена!")

# Вставь сюда свой список имён файлов
filenames = [
"matematika.py",
"fizika.py",
"biologiya.py",
"khimiya.py",
"geografiya.py",
"astronomiya.py",
"informatika.py",
"literatura.py",
"lingvistika.py",
"istoriya.py",
"filosofiya.py",
"psikhologiya.py",
"ekonomika.py",
"politika.py",
"sotsiologiya.py",
"logika.py",
"statistika.py",
"geometriya.py",
"algebra.py",
"trigonometria.py",
"kompyutery.py",
"noutbuki.py",
"smartfony.py",
"tekhnologii.py",
"programmirovanie.py",
"vebrazrabotka.py",
"frontend.py",
"backend.py",
"bazydannykh.py",
"iskusstvennyyintellekt.py",
"neironnye_seti.py",
"mashinnoeobuchenie.py",
"analitikadannykh.py",
"robototekhnika.py",
"internetveshchey.py",
"mobilnyeprilozheniya.py",
"igrirazrabotka.py",
"geymdev.py",
"unity.py",
"unrealengine.py",
"gity.py",
"terminal.py",
"linux.py",
"windows.py",
"macos.py",
"android.py",
"ios.py",
"bezopasnost.py",
"kriptografiya.py",
"seti.py",
"servera.py",
"hosting.py",
"oblakatechnologii.py",
"virtualizatsiya.py",
"docker.py",
"kubernetes.py",
"devops.py",
"testirovanie.py",
"avtomatizatsiya.py",
"api.py",
"restapi.py",
"graphql.py",
"html.py",
"css.py",
"javascript.py",
"typescript.py",
"python.py",
"java.py",
"csharp.py",
"cpp.py",
"golang.py",
"rust.py",
"php.py",
"sql.py",
"nosql.py",
"mongodb.py",
"postgresql.py",
"mysql.py",
"sqlite.py",
"redis.py",
"firebase.py",
"blokchain.py",
"kriptovalyuty.py",
"bitcoin.py",
"ethereum.py",
"defi.py",
"nft.py",
"finansy.py",
"investitsii.py",
"fondoviyrynok.py",
"banki.py",
"kredity.py",
"strakhovanie.py",
"byudzhetirovanie.py",
"nalogi.py",
"ekonomiyadeneg.py",
"lichnyefinansy.py",
"biznes.py",
"startapy.py",
"marketing.py",
"reklama.py",
"smm.py",
"seo.py",
"kontentmarketing.py",
"kopiraiting.py",
"blogging.py",
"youtube.py",
"streaming.py",
"twitch.py",
"tik_tok.py",
"instagram.py",
"vk.py",
"telegram.py",
"discord.py",
"kommunikatsii.py",
"prezentatsii.py",
"softskills.py",
"time_management.py",
"produktivnost.py",
"motivatsiya.py",
"psikhologicheskoezdorovye.py",
"stress.py",
"meditatsiya.py",
"zdorove.py",
"fizkultura.py",
"sport.py",
"fitnes.py",
"yoga.py",
"pitaniye.py",
"dieta.py",
"son.py",
"biohaking.py",
"meditsina.py",
"anatomia.py",
"farmatsiya.py",
"virusologiya.py",
"immunologiya.py",
"vaktsiny.py",
"pandemii.py",
"kliniki.py",
"diagnostika.py",
"lechenie.py",
"surgery.py",
"zabolevaniya.py",
"psikhoterapiya.py",
"obrazovanie.py",
"shkola.py",
"vuz.py",
"ucheba.py",
"kursy.py",
"samoobrazovanie.py",
"uchebniki.py",
"praktika.py",
"ekzameny.py",
"ege.py",
"oge.py",
"olimpiady.py",
"naushnyeissledovaniya.py",
"eksperimenty.py",
"teoriya.py",
"praktika2.py",
"karera.py",
"rezume.py",
"sovetysobesedovanie.py",
"rabota.py",
"freelance.py",
"vakansii.py",
"rezyume.py",
"linkedin.py",
"office.py",
"excel.py",
"word.py",
"powerpoint.py",
"notion.py",
"slack.py",
"jira.py",
"figma.py",
"design.py",
"uiux.py",
"grafikadizayn.py",
"foto.py",
"video.py",
"montazh.py",
"animatsiya.py",
"3d.py",
"modelirovanie.py",
"ar.py",
"vr.py",
"kino.py",
"serialy.py",
"muzyka.py",
"albomy.py",
"koncerty.py",
"instrumenty.py",
"gitary.py",
"fortepiano.py",
"sintezator.py",
"vokal.py",
"rap.py",
"rok.py",
"pop.py",
"klassika.py",
"jaz.py",
"elektronika.py",
"edm.py",
"housemusic.py",
"punkrock.py",
"indierock.py",
"metall.py",
"grunge.py",
"blues.py",
"country.py",
"reggae.py",
"kpop.py",
"jpop.py",
"filmproduction.py",
"kinosnyatie.py",
"scenariy.py",
"rezhissura.py",
"operator.py",
"svet.py",
"zvukozapisy.py",
"dubbing.py",
"aktery.py",
"casting.py",
"kinokritika.py",
"kinopremii.py",
"oscars.py",
"cannes.py",
"filmmaking.py",
"muzey.py",
"vystavki.py",
"iskusstvo.py",
"zhivopis.py",
"skulptura.py",
"grafika.py",
"arhitektura.py",
"dizayninternov.py",
"landshaft.py",
"urbanistika.py",
"stroitelstvo.py",
"remont.py",
"kvartira.py",
"dom.py",
"dacha.py",
"interer.py",
"mebel.py",
"kuhnya.py",
"vanna.py",
"spalnya.py",
"gostinaya.py",
"osveshchenie.py",
"teplo.py",
"konditsioner.py",
"santekhnika.py",
"stroymaterialy.py",
"instrumenty.py",
"elektrika.py",
"bezopasnostdoma.py",
"videonablyudenie.py",
"umnyydom.py",
"homeassistant.py",
"alexa.py",
"siri.py",
"iot.py",
"tehnika.py",
"bytovaya.py",
"holodilnik.py",
"mikrovolnovka.py",
"plita.py",
"stiralnaya.py",
"pylesos.py",
"klimat.py",
"elektronika.py",
"televizory.py",
"monitory.py",
"naushniki.py",
"kolonki.py",
"audiotekhnika.py",
"fotoapparaty.py",
"videokamery.py",
"geyming.py",
"konsoli.py",
"playstation.py",
"xbox.py",
"nintendo.py",
"steam.py",
"epicgames.py",
"onlineigry.py",
"shutery.py",
"strategii.py",
"rpg.py",
"mmo.py",
"mobilnyeigry.py",
"puzzle.py",
"gonki.py",
"fighting.py",
"simulyatory.py",
"vizualnienovelly.py",
"streamingigry.py",
"gamepads.py",
"klaviatury.py",
"myshki.py",
"monitoryigrovy.py",
"vrheadsets.py",
"gamingchairs.py",
"modding.py",
"twitchstream.py",
"youtubeigry.py",
"letplay.py",
"tournaments.py",
"esports.py",
"dota2.py",
"csgo.py",
"valorant.py",
"leagueoflegends.py",
"fortnite.py",
"pubg.py",
"apexlegends.py",
"genshinimpact.py",
"roblox.py",
"minecraft.py",
"sandbox.py",
"konstruktory.py",
"lego.py",
"arduino.py",
"raspberrypi.py",
"elektronnyekomponenty.py",
"3dpechat.py",
"cnc.py",
"mehanika.py",
"avtomatika.py",
"elektrotekhnika.py",
"roboty.py",
"drony.py",
"kvadrokoptery.py",
"aviatsiya.py",
"kosmos.py",
"issledovaniyakosmosa.py",
"spacex.py",
"nasa.py",
"kosmonavty.py",
"mezhplanetnye.py",
"issledovaniya.py",
"mars.py",
"luna2.py",
"sputnik2.py",
"orbity.py",
"mezhzvezdnoe.py",
"teleskopy.py",
"kosmicheskayafizika.py",
"teoriyaotnositelnosti.py",
"kvantovayafizika.py",
"atomy.py",
"yadra.py",
"fizikaelementarnykh.py",
"energiyayadra.py",
"termodinamika.py",
"mekhanika.py",
"optyka.py",
"volny.py",
"zvukovayafizika.py",
"svet.py",
"lazery.py",
"fotonika.py",
"elektromagnetizm.py",
"soprotivlenie.py",
"zaryady.py",
"pole.py",
"elektroenergiya.py",
"elektrostantsii.py",
"gidroenergiya.py",
"vetroenergiya.py",
"solnechnayatekh.py",
"atomnayatekh.py",
"neft.py",
"gaz.py",
"ugol.py",
"alternativnaya.py",
"ekologiya.py",
"klimat.py",
"izmenenie.py",
"resursy.py",
"pererabotka.py",
"zelenye_tekhnologii.py",
"ustoychivoe_razvitie.py",
"zero_waste.py",
"ekoaktivizm.py",
"volontery.py",
"dobrovolchestvo.py",
"blagotvoritelnost.py",
"obshchestvo.py",
"sotsialnyeseti.py",
"media.py",
"zhurnalistika.py",
"novosti.py",
"pressa.py",
"intervyu.py",
"dokumentalnoe.py",
"publitsistika.py",
"publichnyevystupleniya.py",
"rechi.py",
"debates.py",
"oratorstvo.py",
"smi.py",
"televidenie.py",
"radio.py",
"podcasty.py",
"blogi.py",
"vlogi.py",
"novostnoyportal.py",
"forumy.py",
"chaty.py",
"kommentarii.py",
"tsenzura.py",
"svobodaslova.py",
"pravo.py",
"zakon.py",
"konstitutsiya.py",
"sud.py",
"advokaty.py",
"notarius.py",
"ugolovnoepravo.py",
"grazhdanskoepravo.py",
"trudovoepravo.py",
"semeinoyepravo.py",
"nasledstvo.py",
"konflikty.py",
"mediatsiya.py",
"ugolovnye_dela.py",
"sudyebnayasistema.py",
"prokuratura.py",
"politsiya.py",
"pravookhraniteli.py",
"pravozashchita.py",
"prava_cheloveka.py",
"internacionalnoepravo.py",
"mirovayapolitika.py",
"diplomatiya.py",
"oon.py",
"nato.py",
"es.py",
"ssha.py",
"rossiya.py",
"kitay.py",
"india.py",
"afrika.py",
"blizhniyvostok.py",
"ukraina.py",
"voennyevoprosy.py",
"vooruzheniye.py",
"bezopasnostvstrane.py",
"armeiya.py",
"voennaya_tekhnika.py",
"geopolitika.py",
"istoriya_vojny.py",
"istoriyamira.py",
"kulturnoenasledie.py",
"tradicii.py",
"religiya.py",
"filosofy.py",
"etika.py",
"moral.py",
"kultura.py",
"iskusstvo_v_mire.py",
"natsionalnyekultury.py",
"prazdniki.py",
"obychai.py",
"narodnye_tantsy.py",
"folklor.py",
"literaturnyezhanry.py",
"proza.py",
"poeziya.py",
"drama.py",
"fantastika.py",
"detektivy.py",
"romany.py",
"klassika.py",
"sovremennaya_literatura.py",
"knigi.py",
"avtory.py",
"knizhnyeklub.py",
"chitateli.py",
"knizhnyerezensii.py",
"knigoizdanie.py",
"elektronnyeknigi.py",
"audioknigi.py",
"chtenie.py",
"obrazovanie_21vek.py",
"onlayn_obuchenie.py",
"kursyprogrammirovaniya.py",
"shkolnye_predmety.py",
"uchebnye_platformy.py",
"udemy.py",
"coursera.py",
"stepik.py",
"skillbox.py",
"geekbrains.py",
"youtube_obuchenie.py",
"tik_tok_edu.py",
"instagram_kursy.py",
"lichnayy_rost.py",
"samoocenka.py",
"emotsionalny_intellekt.py",
"obshchenie.py",
"otnosheniya.py",
"drugi.py",
"semya.py",
"roditeli.py",
"vospitanie.py",
"deti.py",
"podrostki.py",
"shkolniki.py",
"studenty.py",
"rabotodateli.py",
"kollektiv.py",
"teamwork.py",
"liderstvo.py",
"startup_komanda.py",
"biznes_idei.py",
"prodvizhenie.py",
"prodazhi.py",
"klienty.py",
"servis.py",
"konsultatsii.py",
"feedback.py",
"reputatsiya.py",
"kliyentskiy_opyt.py",
"biznes_modeli.py",
"franshizy.py",
"marketplace.py",
"elektronnayatorgovlya.py",
"internetmagaziny.py",
"amazon.py",
"ozon.py",
"wildberries.py",
"aliexpress.py",
"ebay.py",
"marketology.py",
"analitikarynka.py",
"konkurenty.py",
"niche.py",
"productmarketfit.py",
"razvitie.py",
"scaleup.py",
"exit.py",
"investory.py",
"venchurfondy.py",
"crowdfunding.py",
"kickstarter.py",
"patenty.py",
"avtorskoepravo.py",
"intellekt_sobstvennost.py",
"brendy.py",
"firmennyy_stil.py",
"logotipy.py",
"upakovka.py",
"reklamnye_roliki.py",
"targeting.py",
"kontekstnaya_reklama.py",
"seo_strategiya.py",
"sem.py",
"email_marketing.py",
"newsletter.py",
"avtomatizatsiya_biznesa.py",
"buhgalteriya.py",
"1c_predpriyatie.py",
"zarplata_i_kadry.py",
"otchetnost.py",
"nalogovaya.py",
"audit.py",
"finmonitoring.py",
"finotchetnost.py",
"kriptobuhgalteriya.py",
"fintech.py",
"bankovskie_uslugi.py",
"mobilnyy_banking.py",
"karty.py",
"kredity_dlya_biznesa.py",
"ipotechnoe_kreditovanie.py",
"kreditnaya_istoriya.py",
"finansovye_riski.py",
"strahovye_sluchai.py",
"dorozhnaya_strakhovka.py",
"zdorovie_i_strakhovanie.py",
"turistskaya_strakhovka.py",
"finansovoe_planirovanie.py",
"investirovanie_vnedvizhimost.py",
"arenda.py",
"pokupka_kvartiry.py",
"ipoteka.py",
"zhkkh.py",
"kvartplata.py",
"upravlyayushchaya_kompaniya.py",
"remont_kvartiry.py",
"vnutrennyaya_otdelka.py",
"dizayn_remonta.py",
"stroitelstvo_doma.py",
"fundament.py",
"krysha.py",
"otoplenie.py",
"ventilyatsiya.py",
"okna.py",
"dveri.py",
"mebel_na_zakaz.py",
"interer_pod_kluch.py",
"umnyy_interer.py",
"domashniy_ofis.py",
"kompyuternaya_mebel.py",
"osveshchenie_v_interere.py",
"dekor.py",
"domashniye_rasteniya.py",
"sad_i_ogorod.py",
"ogorodnichestvo.py",
"teplica.py",
"poliv.py",
"udobreniya.py",
"zashchita_rasteniy.py",
"kompost.py",
"sadovye_instrumenty.py",
"dachnyy_sezon.py",
"sadovaya_mebel.py",
"peyzazhnyy_dizayn.py",
"besedki.py",
"barbekyu.py",
"gril.py",
"otdykh_na_prirode.py",
"pikniki.py",
"palatki.py",
"poezdki.py",
"avtoputeshestvie.py",
"turizm.py",
"poisk_aviabiletov.py",
"bronirovanie.py",
"oteli.py",
"airbnb.py",
"gidy.py",
"jekskursii.py",
"mestnye_kukhni.py",
"kulinarniye_tury.py",
"ekoturizm.py",
"trekking.py",
"alpinism.py",
"gory.py",
"more.py",
"plavanie.py",
"plyazhi.py",
"snorkeling.py",
"dayving.py",
"priklyucheniya.py",
"ekspeditsii.py",
"nablyudenie_za_zhivotnymi.py",
"safari.py",
"arktika.py",
"antarktida.py",
"severny_polyus.py",
"ostrova.py",
"karaiby.py",
"yuzhnaya_amerika.py",
"afrika_tury.py",
"evropa.py",
"aziya.py",
"rossiya_puteshestviya.py",
"sibir.py",
"ural.py",
"kavkaz.py",
"dalniy_vostok.py",
"baikal.py",
"altay.py",
"kamchatka.py",
"zolotoe_koltso.py",
"moskva.py",
"sankt_peterburg.py",
"goroda_rossii.py",
"kulturnye_meropriyatiya.py"
"koncerty_v_rossii.py",
"festivali.py",
"teatry.py",
"balet.py",
"muzykalnye_teatry.py",
"detskaya_scena.py",
"kinopokazy.py",
"kinofestivali.py",
"dokumentalnye_filmy.py",
"nezavisimoe_kino.py",
"rossiyskoe_kino.py",
"zarubezhnoe_kino.py",
"aktery_i_aktrisy.py",
"rezhissery.py",
"stsena.py",
"kinostudii.py",
"ozvuchka.py",
"specialnye_effekty.py",
"grafika_v_kino.py",
"3d_animatsiya.py",
"vizualnye_effekty.py",
"videomontazh.py",
"kinomontazh.py",
"treningi.py",
"seminary.py",
"konferentsii.py",
"vebinary.py",
"master_klass.py",
"obuchenie_online.py",
"sertifikaty.py",
"prokachka_navikov.py",
"kariernye_konsultatsii.py",
"personal_brand.py",
"portfolio.py",
"motivatsionnoe_pismo.py",
"sovety_po_karere.py",
"rabota_na_frilanse.py",
"zakazchiki.py",
"kak_nayti_klientov.py",
"freelance_platformy.py",
"upwork.py",
"freelancer.py",
"kwork.py",
"habr_freelance.py",
"disayn_na_zakaz.py",
"veb_dizayn.py",
"logotipy_na_zakaz.py",
"graficheskiy_dizayn.py",
"moukapy.py",
"figma_praktika.py",
"interfeysy.py",
"prototipirovanie.py",
"user_experience.py",
"user_interface.py",
"testirovanie_dizayna.py",
"product_dizayn.py",
"ilustratsii.py",
"risovanie_na_planshete.py",
"digital_art.py",
"komiksy.py",
"manga.py",
"artbooki.py",
"pechatnaya_produktsiya.py",
"vizitki.py",
"buklety.py",
"broshyury.py",
"katalogi.py",
"upakovka_tovarov.py",
"torgovaya_marka.py",
"marketpleysy.py",
"marketolog_na_freelance.py",
"smm_strategiya.py",
"targetirovannaya_reklama.py",
"insta_reklama.py",
"vk_target.py",
"facebook_ads.py",
"tiktok_ads.py",
"youtube_kanal.py",
"razvitie_kanala.py",
"monetizatsiya.py",
"donaty.py",
"patreon.py",
"boosty.py",
"zen_kanal.py",
"telegram_kanal.py",
"chat_boty.py",
"avtomatizatsiya_chatov.py",
"ai_skripty.py",
"midjourney.py",
"stabil_diffusion.py",
"ai_v_dizayne.py",
"ai_v_kontente.py",
"generatsiya_kontenta.py",
"teksty_na_zakaz.py",
"kopiraiting_dlya_saytov.py",
"seo_kopiraiting.py",
"lendingy.py",
"stranitsy_prodazh.py",
"konversii.py",
"analitika_sayta.py",
"google_analytics.py",
"yandex_metrika.py",
"heatmaps.py",
"ab_testy.py",
"optimizatsiya_stranits.py",
"user_journey.py",
"konversiya.py",
"povedenie_polzovateley.py",
"ux_issledovaniya.py",
"lichnye_finansy.py",
"byudzhetirovanie.py",
"koplenie_sredstv.py",
"investitsii_dlya_nachinayushchih.py",
"kriptovalyuty.py",
"bitcoin.py",
"ethereum.py",
"kriptokoshelki.py",
"nft.py",
"blokcheyn.py",
"defi.py",
"kriptotorgovlya.py",
"kriptobirzhi.py",
"kriptobezopasnost.py",
"metavers.py",
"web3.py",
"digital_identity.py",
"virtualnaya_realnost.py",
"augmented_reality.py",
"realnost_i_tehnologii.py",
"tehnologii_budushchego.py",
"iskusstvennyy_intellekt.py",
"machine_learning.py",
"deep_learning.py",
"neural_seti.py",
"kompyuternoe_zrenie.py",
"obrabotka_teksta.py",
"nlu.py",
"nlg.py",
"chatgpt.py",
"openai.py",
"yandex_gpt.py",
"ai_in_business.py",
"ai_v_marketinge.py",
"ai_v_meditsine.py",
"ai_v_obrazovanii.py",
"ai_v_bytovoy_zhizni.py",
"ai_v_igrakh.py",
"ai_v_zvuke.py",
"ai_v_grafike.py",
"generativnyy_ai.py",
"stable_diffusion_art.py",
"prompt_engineering.py",
"prompt_konstruktor.py",
"avtomatizatsiya_rutiny.py",
"obshchenie_s_ai.py",
"ai_assistenty.py",
"tekhnologii_umnogo_doma.py",
"smart_home_gadgets.py",
"umnyy_holodilnik.py",
"umnaya_kolonka.py",
"umnyy_televizor.py",
"umnyy_domofon.py",
"iot_ustroystva.py",
"seti_5g.py",
"wi_fi_6.py",
"mobilnye_seti.py",
"sotovaya_svyaz.py",
"svyaz_v_budushchem.py",
"razrabotka_prilozheniy.py",
"mobilnaya_razrabotka.py",
"android_studio.py",
"xcode_ios.py",
"flutter.py",
"react_native.py",
"krossplatforma.py",
"frontend.py",
"backend.py",
"fullstack.py",
"html_css_js.py",
"typescript.py",
"react_js.py",
"vue_js.py",
"svelte.py",
"node_js.py",
"express_js.py",
"django.py",
"flask.py",
"fastapi.py",
"postgresql.py",
"mongodb.py",
"mysql.py",
"redis.py",
"graphql.py",
"restapi.py",
"docker.py",
"kubernetes.py",
"devops.py",
"github_actions.py",
"ci_cd.py",
"vcs_git.py",
"unit_testy.py",
"pytest.py",
"selenium.py",
"testirovanie_ui.py",
"manual_testing.py",
"qa_engineer.py",
"bug_tracking.py",
"jira.py",
"agile.py",
"scrum.py",
"kanban.py",
"task_manager.py",
"notion.py",
"trello.py",
"monday_com.py",
"product_manager.py",
"ux_writer.py",
"bizdev.py",
"hr_tehnologii.py",
"rekruting.py",
"soprovozhdenie_sotrudnikov.py",
"korporativnaya_kultura.py",
"onboarding.py",
"tim_bilding.py",
"psikhologiya_komandy.py",
"emotsionalnoe_vygoranie.py",
"mentalnoe_zdorovye.py",
"psikhoterapiya.py",
"samopodderzhka.py",
"rezhim_dnya.py",
"son.py",
"sport.py",
"zdorovoe_pitanie.py",
"veganstvo.py",
"vegetarianstvo.py",
"keto.py",
"intermittent_fasting.py",
"nabor_massy.py",
"pohudenie.py",
"trenirovki_doma.py",
"zaryadka.py",
"fitnes_klub.py",
"krossfit.py",
"yoga.py",
"stretching.py",
"plavanie_zanyatiya.py",
"boevye_iskusstva.py",
"boks.py",
"mma.py",
"karate.py",
"dzhiu_dzhitsu.py",
"kendo.py",
"sportsmeny.py",
"olimpiyskie_igry.py",
"chempionaty.py",
"sportivnaya_ekipirovka.py",
"zdorovye_sustavy.py",
"profilaktika_travm.py",
"meditsina_sporta.py",
"biokhimiya.py",
"biologiya.py",
"anatomia.py",
"fiziologiya.py",
"genetika.py",
"kletki.py",
"DNK.py",
"genomika.py",
"epigenetika.py",
"sintez_belkov.py",
"mutatsii.py",
"biotekhnologii.py",
"meditsina_21_vek.py",
"vaktsiny.py",
"immunitet.py",
"antitela.py",
"pandemii.py",
"epidemiologiya.py",
"virusologiya.py",
"mikrobiologiya.py",
"bakterii.py",
"gribki.py",
"antibiotiki.py",
"diagnostika.py",
"kt_mrt.py",
"laboratornye_analizy.py",
"meditsinskoe_oborudovanie.py",
"nosimye_ustroystva.py",
"fitness_trekery.py",
"smart_chasy.py",
"zdravookhranenie.py",
"medtech.py",
"digital_medicine.py",
"telemeditsina.py",
"meditsinskie_sertifikaty.py",
"farmatsevtika.py",
"apteki_online.py",
"meditsinskiy_turizm.py",
"zdorovyy_obraz_zhizni.py",
"psikhologicheskoe_zdorovye.py",
"lichnaya_effektivnost.py",
"planirovanie_dnya.py",
"postanovka_tsely.py",
"dostizhenie_rezultatov.py",
"motivatsiya.py",
"tselustremlyonnost.py",
"rabota_nad_oshibkami.py",
"obratnaya_svyaz.py",
"samoanaliz.py",
"reflleksiya.py",
"emotsii.py",
"vzaimootnosheniya.py",
"nastroenie.py",
"samoregulyatsiya.py",
"osoznannost.py",
"meditatsiya.py",
"dyhatelnye_praktiki.py",
"praktika_blagodarnosti.py",
"dnevnik.py",
"vedenie_zapisey.py",
"tsifrovoy_detoks.py",
"sokrashchenie_stressa.py",
"priroda_kak_terapiya.py",
"kreativnost.py",
"vizualizatsiya_tseley.py",
"myshlenie_rasta.py",
"zivotnie.py",
"kompeteri.py",
"recepti.py",
"posuda.py",
"tekhniki.py",
"snaryad.py",
"poezda.py",
"autobusi.py",
"pokupki.py",
"produkti.py",
"uvelicheniye.py",
"ustroystva.py",
"diski.py",
"samovyvoz.py",
"psikhologi.py",
"medicina.py",
"tovarov.py",
"dostavka.py",
"skidki.py",
"sozdanie.py",
"razdel.py",
"ekspertiza.py",
"dlya_podroste.py",
"roboty.py",
"obmen.py",
"skidka.py",
"otzyvy.py",
"prosto.py",
"prazdniki.py",
"pervichnoye.py",
"kompaniya.py",
"forumi.py",
"katastrofi.py",
"otoplenie.py",
"polet.py",
"siberia.py",
"chemistry.py",
"kolledzhi.py",
"mineralnye.py",
"palatki.py",
"volontyorstvo.py",
"otnosheniya.py",
"vstrechi.py",
"nastroyki.py",
"liudi.py",
"sait.py",
"birzhi.py",
"gnomy.py",
"dostizheniya.py",
"kivka.py",
"tikhie.py",
"domiki.py",
"metody.py",
"ekstremalnye.py",
"stoliki.py",
"tech_volontyorstvo.py",
"kultura.py",
"vodovoz.py",
"napravleniya.py",
"segodnya.py",
"technologii.py",
"morye.py",
"citaty.py",
"chestnie.py",
"informacii.py",
"mirki.py",
"spetsialisti.py",
"seti.py",
"kreativ.py",
"komplekt.py",
"izgotovlenie.py",
"proekty.py",
"monitoring.py",
"nastupaiushchee.py",
"metody_issledovaniya.py",
"otlichiya.py",
"izmenenie.py",
"sostavlyayushchie.py",
"iskusstvenniy.py",
"scenarii.py",
"tehnicheskie.py",
"sozdaniya.py",
"projekty.py",
"ekspansiya.py",
"oborudovanie.py",
"soglasovanie.py",
"testirovki.py",
"webinar.py",
"kompanii.py",
"reestr.py",
"tseny.py",
"oformlenie.py",
"tema.py",
"velosipedi.py",
"tury.py",
"tvorchestvo.py",
"samouchka.py",
"smi.py",
"knigi.py",
"materialy.py",
"obzory.py",
"raznoe.py",
"rabatka.py",
"tekhniki_rabotyi.py",
"dostupnosti.py",
"programmnye.py",
"sovety.py",
"rabotniki.py",
"testirovanie.py",
"ispolnitel.py",
"samodielka.py",
"izmerenie.py",
"strakhovanie.py",
"optimizatsiya.py",
"sovmeshchenie.py",
"editirovanie.py",
"dizajn_intererov.py",
"plastik.py",
"programmy.py",
"voennaia.py",
"programy_rabotayut.py",
"pokupateli.py",
"proektirovanie.py",
"sistemnyye.py",
"razmetka.py",
"inzheneriya.py",
"avtoelektrika.py",
"proverki.py",
"izmeritel.py",
"adaptatsiya.py",
"vibratory.py",
"produktov.py",
"tovaryi.py",
"uslugi.py",
"planovanie.py",
"razvlecheniya.py",
"ekologiya.py",
"chistota.py",
"trekking.py",
"velosipedi2.py",
"podklyucheniye.py",
"tsikly.py",
"zashchita.py",
"izdelie.py",
"kombinatsii.py",
"otvetstvennost.py",
"raznoobraznye.py",
"text_3.py",
"ideal.py",
]

# Проходим по всем именам файлов и создаём пустые файлы
for name in filenames:
    file_path = os.path.join(folder_path, name)
    # Если файл уже существует, можно его пропустить
    if os.path.exists(file_path):
        print(f"Файл {name} уже существует, пропускаем.")
    else:
        with open(file_path, 'w', encoding="utf-8") as f:
            pass  # Файл создаётся пустым. При необходимости можно добавить шаблон содержимого.
        print(f"Файл {name} создан в папке '{folder_path}'.")
