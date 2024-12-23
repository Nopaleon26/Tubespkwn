# Define the characters with colors
define a = Character("Anita", color="#FF69B4")  # Pink color for Anita
define an = Character("Atasan", color="#FFD700") # Gold color for Atasan
define d = Character("Dita", color="#1E90FF")   # Blue color for Dita
define dy = Character("Dypho", color="#32CD32") # Green color for Dypho
define b = Character("Baithar", color="#FFD700") # Gold color for Baithar
define n = Character("", color="#A9A9A9") # Grey color for Narrator
define r = Character("Rama", color="#FF4500") # Orange color for Rama
define p = Character("Pak Warung", color="#FFD700") # Gold color for Pak Warung
define t1 = Character("Teman 1", color="#FF4500") # Orange color for Teman 1
define t2 = Character("Teman 2", color="#FF4500") # Orange color for Teman 2

# Define the images
image bg_dining_room = im.Scale("dapur.png", config.screen_width, config.screen_height)
image garasi = im.Scale("garasi.png", config.screen_width, config.screen_height)
image kamar = im.Scale("kamar.jpg", config.screen_width, config.screen_height)
image kantor = im.Scale("Kantor.jpg", config.screen_width, config.screen_height)
image kelas = im.Scale("kelas.png", config.screen_width, config.screen_height)
image parkiran_sekolah = im.Scale("parkiran sekolah.png", config.screen_width, config.screen_height)
image pecel_lele = im.Scale("pecel lele 2.jpg", config.screen_width, config.screen_height)
image ruang_keluarga = im.Scale("ruang keluarga.jpg", config.screen_width, config.screen_height)
image bapak = im.Scale("bapak.png", 540, 1164) 
image dita = im.Scale("dita.png", 256, 384)   
image anita = im.Scale("anita.png", 650, 1000)  
image dypho = im.Scale("dypho.png", 450, 933) 
image rama = im.Scale("rama.png", 622, 933) 
image teman1 = im.Scale("cewe 1.png", 533, 800) 
image teman2 = im.Scale("cewe 2.png", 400, 600) 
image Atasan = im.Scale("Atasan.png", 250, 500) 
image text = Text("Waktu makan malam sudah tiba. Anita, Dypho, dan Dita telah berkumpul di meja makan. \nNamun, 1 kursi masih belum terisi.{w}", size = 22)

# Define the transitions
define dissolve = Dissolve(1.0)
define fade = Fade(1.0, 0.5, 1.0)

# Start the script
label start:
    #cerita singkat 
    show text at Transform(xpos=150, ypos=300) with dissolve
    pause
    # Intro
    scene bg_dining_room with fade
    play music "Intro(1).mp3" fadeout 1

    # Show the characters with their images and transitions
    show anita at Transform(xpos=-50, ypos=200,) with moveinleft
    show dypho at Transform(xpos=0.5, ypos=150, xanchor=0.5) with dissolve
    show dita at Transform(xpos=900, ypos=250) with moveinright

    play sound "scene(1)_makan di dapur.mp3"
    queue sound "scene(1)_makan di dapur.mp3"

    d "Ibu, Ayah belum pulang?"
    a "Kak, tolong telepon Ayah."
    dy "Baik, Ibu."
    n "Yang dimintai tolong pun menurut."
    play sound "sfx_phone_calling.mp3"
    n "\"Nomor yang Anda tuju sedang tidak aktif atau berada di luar jangkauan.\""
    n "Dypho kembali menghubungi Ayahnya."
    n "Nihil, panggilannya lagi-lagi tidak diangkat."
    a "Mungkin Ayah lembur dan lagi gak bisa diganggu. Kita makan duluan aja."

    # Hide the characters
    hide anita with dissolve
    hide dypho with dissolve
    hide dita with dissolve

    # narration
    n "Pagi hari ini ternyata adalah saat terakhir Anita menyiapkan secangkir kopi untuk suaminya dan Dypho beserta Dita diantarkan ke sekolah oleh Baithar."
    n "Sejak malam itu, Baithar tidak pernah kembali ke rumah. Eksistensinya hilang tanpa kabar."
    n "Lantas, kemanakah Baithar pergi? Lalu, bagaimana Anita dan Dypho melanjutkan kehidupannya?"

    # The Game now give a choice to play in Dypho perspective or Anita perspective
    menu:
        "Mainkan sebagai Dypho":
            jump dypho_pov
        "Mainkan sebagai Anita":
            jump anita_pov
    
    # Dypho's perspective
    label dypho_pov:
        play music "scene(2)_dypho_bangun.mp3" fadeout 1
        scene kamar with fade

        play sound "sfx_alarm.mp3"
        n "(suara alarm)"
        show dypho at Transform(xpos=0.5, ypos=10, xanchor=0.5) with dissolve
        n "Perlahan Dypho bangkit dari kasurnya. Dilihatnya jam di dinding kamar."
        n "Jam 06.20!"
        n "Segera dia berlari ke kamar Dita untuk membangunkannya."
        dy "Dita, bangun! Kau mau sekolah gak?!"
        show dita at right with dissolve
        d "Duh, jam berapa ini?"
        dy "Jam setengah 7! Ayo siap-siap."

        hide dita with dissolve
        n "Dypho segera memakai seragamnya."
        dy "Bodo amat soal mandi, tidak sempat, aku harus mengantar Dita ke SD-nya dan sampai di sekolah sebelum jam 7."
        dy "Oh iya, apakah ibu sudah bangun? Seharusnya ibu pergi bekerja pukul 7 supaya tidak terlambat karena jalanan macet ibukota."
        n "Perlahan Dypho membuka pintu kamar ibu."
        n "Dia masih tertidur, dengan baju yang dia pakai untuk bekerja kemarin."

        scene kamar with fade
        show dypho at Transform(xpos=0.5, ypos=10, xanchor=0.5) with dissolve
        n "Bangunkan Ibu?"
        menu:
            "Ya":
                n "Dypho memutuskan untuk membangunkan ibunya."
                jump wake_mother
            "Tidak":
                n "Dypho memutuskan untuk tidak membangunkan ibunya."
                jump dont_wake_mother

    label wake_mother:
        show anita at Transform(xpos=0.0, ypos=200) with dissolve
        dy "Bu, bangun, bu. Sudah setengah 7, ibu kan harus siap-siap."
        n "Anita hanya menggeliat, tangannya memberi isyarat agar Dypho keluar dari kamarnya."
        n "Dypho menghela napas, perlahan keluar dan menutup pintu kamar ibunya."
        hide anita with dissolve
        jump dypho_pov_continued

    label dont_wake_mother:
        n "Dypho menggeleng dan menutup pintu kamar ibunya."
        dy "Sudahlah, sepertinya ibu sangat lelah setelah kemarin bekerja."
        jump dypho_pov_continued

    label dypho_pov_continued:
        scene ruang_keluarga with fade
        show dypho at Transform(xpos=0.5, ypos=150, xanchor=0.5) with dissolve

        dy "Sial, sudah jam 07.35!"
        dy "Ditaaa!! kamu sudah siap belum? Hari ini aku harus masuk jam 7."

        show dita at right with dissolve

        d "Belum kakk."
        dy "Kamu lagi apa sih? Ayo buruan! Aku tunggu di luar ya."
        d "Iyaa, ini bentar lagi."
        n "Dypho memutuskan keluar duluan untuk mengeluarkan motornya dari garasi."

        scene garasi with fade
        show dypho at Transform(xpos=0.5, ypos=200, xanchor=0.5) with dissolve

        n "5 menit kemudian Dita berlari keluar rumah dan mendapati kakaknya sudah siap di atas motornya."
        
        show dita at right with dissolve
        dy "Lelet!"
        dy "Pokoknya kalau aku telat, kamu harus tanggung jawab."
        d "Suruh siapa telat bangunin!"
        n "Tanpa memperpanjang perdebatan Dypho langsung mengendarai motornya."
        play sound "sfx_motor.mp3"
        n "(suara motor)"

        scene parkiran_sekolah with fade
        play music "scene_sekolah.mp3" fadeout 1
        show dypho at Transform(xpos=0.5, ypos=200, xanchor=0.5) with dissolve

        play sound "sfx_bel_sekolah.mp3"
        n "(suara bel sekolah)"
        dy "Hhhhh, hampir saja terlambat."

        show rama at Transform(xpos=0.0, ypos=215, xanchor=0.0) with dissolve

        r "Hei, Dy."
        dy "Hei, baru nyampe juga?"
        r "Iya, baru aja."

        r "Eh, kamu udah ngerjain PR dari pak Irfan?"
        dy "PR matematika? Udah dong."
        r "Mau nyontek dong, hehe."

        menu:
            "Berikan contekan":
                dy "Mmm, bo..leh deh. Ni."
                show dypho at Transform(xpos=0.5, ypos=200, xanchor=0.5) with dissolve
                show rama at Transform(xpos=0.0, ypos=200, xanchor=0.0) with dissolve
                r "Makasih, Dy! Kamu emang temen terbaik."
                dy "Sebenarnya aku tahu ini tidak benar, tapi mau bagaimana lagi."

            "Tidak memberikan contekan":
                dy "Yeuuh, enak saja. Aku mengerjakan ini susah payah, dan kamu mau nyontek? Ga boleh."
                r "Ah, pelit."
                dy "Hahaha, tapi kalau kamu mau, aku bisa ngajarin kamu. Kelas pak Irfan masih lama, aku bisa mengajarimu di jam istirahat."
                r "Serius? Boleh deh."
                dy "Thank you ya, Dy."

        hide rama with dissolve
        hide dypho with dissolve
        n "Seharian itu sekolah berjalan seperti biasa. Dypho sudah siap pulang dan menuju tempat motornya diparkirkan."
        show dypho at Transform(xpos=0.5, ypos=200, xanchor=0.5) with dissolve
        dy "Tunggu, hari apa ini? Selasa? Sial, aku lupa hari ini jadwalku piket."
        dy "Pantas saja seperti ada yang terlewat. Duh, aku malas jalan kembali ke kelas."
        dy "Atau kabur saja ya? Kemarin-kemarin juga ada teman piketku yang tidak ikut membantu."

        menu:
            "Kembali ke kelas untuk piket":
                dy "Hhh, baiklah, kurasa aku harus bertanggung jawab atas kewajibanku."
                scene kelas with fade
                show dypho at Transform(xpos=0.5, ypos=100, xanchor=0.5) with dissolve
                dy "Hai, guys, maaf banget aku hampir lupa kalau hari ini jadwal piketku."
                show teman1 at Transform(xpos=0.0,ypos=100, xanchor=0.0) with dissolve
                show teman2 at Transform(xpos=1.0,ypos=150, xanchor=1.0) with dissolve
                t1 "Eh, Dy. Gapapa, gapapa. Malah respek karena kamu memutuskan untuk balik lagi ke kelas, padahal bisa aja kamu kabur."
                t2 "Asli, Dy. Makasih ya ga kabur. Hari ini kelas lumayan kotor gara-gara kemarin hujan, jadinya banyak lumpur tanah dari sepatu orang-orang."
                dy "Syukur kalo gitu, keputusanku sudah tepat."
                n "Dypho lanjut mengerjakan piket bersama teman-temannya sampai akhirnya kelas dirasa sudah bersih."
                dy "Aku pulang duluan, yaa."
                t1 "Iyaa, hati-hatii."
                t2 "Makasih guys."
                dy "Dadaah."

            "Kabur dari piket":
                dy "Ah, sudahlah. Bolos piket satu kali tidak berpengaruh kan?"

        scene ruang_keluarga with fade
        show dypho at Transform(xpos=0.5, ypos=10, xanchor=0.5) with dissolve
        show dita at right with dissolve

        dy "Hmm? Ibu sepertinya ibu lembur lagi hari ini."
        dy "Ditaa, kamu sudah pulang?"
        d "Iyaa, kak."

        menu:
            "Membeli makanan dari luar":
                dy "Dita, kamu mau makan apa? Biar aku belikan keluar naik motor."
                d "Apa saja lah."
                dy "Dasar cewek, awas saja kalau nanti kamu protes."
                scene pecel_lele with fade
                show dypho at Transform(xpos=0.5, ypos=100, xanchor=0.5) with dissolve
                dy "Pak, kayak biasa ya."
                p "Pecel lele nya 2, tempe tahu 2, sama sate usus nya 2, A?"
                dy "Iya, pak."
                p "Siaap."
                n "Sambil menunggu pesanannya Dypho bermain-main dengan pikirannya."
                play music "scene_sedih.mp3" fadeout 1
                dy "Hhh, akhir-akhir ini keadaan makin sulit. Awal-awal ayah menghilang, ibu masih memiliki setidaknya harapan positif bahwa ayah akan segera kembali."
                dy "Tapi setelah 6 bulan, ibu mulai tampak stress dan kesusahan. Saat itu ibu memutuskan untuk bekerja lagi karena tabungan dari gaji ayah hampir menipis."
                dy "Dan saat itu juga ibu perlahan menjadi orang yang tidak aku kenal."
                dy "Aku bisa memahami kalau pekerjaan ibu di kantor begitu berat. Aku juga paham ibu sedang menjalankan kewajibannya sebagai ibu bagi aku dan Dita, beristirahat setelah bekerja dan di hari libur juga merupakan hak ibu."
                dy "Tapi rasanya tetap ada yang tidak benar. Apalagi Dita terbilang masih kecil, dia berhak mendapat perhatian dari orang tuanya, bukan hanya aku sebagai kakaknya."
                dy "Andaikan ayah masih ada.."
                p "A, jangan melamun! Ini pecel lele nya udah jadi."
                dy "Oh iya, makasih pak."
                p "A, bapakmu tu dari mana aja loh? Ko bertaun-taun pergi, tiba-tiba mampir. Kalian berantem tah? Dulu biasanya kalian berdua mulu toh kalo beli ke sini?"
                dy "Hah?! Apa katanya?! Ayah ke sini?!"
                dy "Bapak yakin itu ayah saya?!"
                p "Yoo, tua-tua gini saya masih inget muka orang walaupun udah ga ketemu lama, A. Yakin saya. Oh iya, bapakmu tadi ngutang 15 ribu, sekalian lah kamu lunasi."
                dy "Tidak mungkin, mana mungkin ayah masih hidup."
                dy "Jangan-jangan tadi aku berpapasan dengannya? Tidak tidak, aku harus memastikannya sendiri."
                scene ruang_keluarga with fade
                show dypho at Transform(xpos=0.5, ypos=100, xanchor=0.5) with dissolve
                dy "Tidak ada, sudah kuduga, yasudahlah."
                dy "Dit, ayo makan malam, aku beli pecel lele."
                d "Asik."

            "Memasak mie":
                dy "Ah, kurasa tidak ada salahnya makan mie instan lagi. Toh Dita juga suka."
                scene bg_dining_room with fade
                show dypho at Transform(xpos=0.5, ypos=100, xanchor=0.5) with dissolve
                show dita at right with dissolve
                dy "Ditaa ayo makan!"
                d "Asiikk."
                d "Mie lagi? Nanti lambungnya keriting loh kalau keseringan."
                dy "Ngaco, kata siapa kayak gitu. Udah, jangan banyak mau."
                n "Tepat ketika mereka duduk di kursi yang mengelilingi meja makan, hujan turun."
                dy "Tiba-tiba hujan."

        play sound "sfx_ketok_pintu.mp3"
        n "Tok tok tok."
        dy "Hm? Siapa yang mengetuk pintu? Apa ibu lupa membawa kunci?"
        play sound "sfx_ketok_pintu.mp3"
        n "TOK TOK TOK."
        dy "Siapaa?"
        n "Dypho bertanya sambil menghampiri pintu, sedangkan Dita takut-takut mengintip dari ruang makan."
        dy "Ibu?"
        n "Dypho mencoba menebak. Tapi sesampainya di depan pintu ia tahu itu bukan ibunya, dari jendela dia bisa melihat siluet si pengetuk pintu, laki-laki."
        dy "Siapa? Tetangga sebelah? Semoga bukan orang aneh."
        n "Dypho memberanikan diri membuka kunci, lalu ia membuka pintu."
        play sound "sfx_kaget.mp3"
        dy "Siapa-"
        n "Dypho tidak bisa melanjutkan kata-katanya."
        n "Orang yang selama ini dikira telah meninggalkan dunia ini, sekarang berdiri di hadapannya. Ucapan tukang lele itu bukan bohongan."
        dy "Ayah?!"

        jump epilog

    # POV Anita

    label anita_pov:
        play music "scene_anita.mp3" fadeout 1
        n "Sejak kepergian Baithar Prawono–suami Anita–, Anita mau tidak mau merangkap “jabatan” sebagai ibu rumah tangga sekaligus pencari nafkah."
        n "Di usianya yang sudah tidak muda, Anita harus mengeluarkan tenaga ekstra untuk mencari dan melamar pekerjaan. Sampai akhirnya, Anita kini bekerja sebagai akuntan."
        n "Setiap hari, Anita mesti berangkat pagi-pagi sekali dan tiba di rumah saat Dypho dan Dita sudah tidur dikarenakan jarak antara rumah dan kantornya cukup jauh."
        n "Hal inilah yang menjadi penyebab Anita sudah tidak sempat menyiapkan sarapan dan makan malam untuk kedua anaknya–bahkan untuk dirinya sendiri pun ia tidak memiliki waktu,"
        n "atau sekadar menanyakan bagaimana hari yang dilalui Dypho dan Dita di sekolah."
        scene pagi_hari with fade
        show anita at Transform(xpos=0.5, ypos=300, xanchor=0.5) with dissolve

        n "Seperti biasa, sebelum berangkat ke kantor, Anita meninggalkan 1 lembar uang dengan nominal 100.000 di atas meja makan lengkap dengan secarik kertas bertuliskan:"
        n "“Uang ini untuk 3 kali makan Kakak dan Dita.”"
        n "Setelah selesai dengan urusannya, Anita bergegas pergi."
        scene kantor with fade
        show anita at Transform(xpos=0.5, ypos=300, xanchor=0.5) with dissolve

        n "Sesampainya di kantor, Anita langsung mengerjakan tugasnya. Aplikasi Microsoft Word dan Excel pada komputer, bolak-balik dibuka oleh Anita guna mencatat transaksi keuangan dan menyusun laporan."
        n "Sesekali Anita meregangkan otot-otot dan memijat pelipisnya karena kelelahan."

        n "Tak terasa, waktu kini menunjukkan pukul 17:00. Tandanya, jam kerja Anita untuk hari ini sudah selesai. Saat Anita memasukkan barang-barangnya ke dalam tas, tiba-tiba atasannya menghampiri."

        show atasan at Transform(xpos=0.0, ypos=10, zoom = 0.5) with dissolve

        an "Anita, tolong selesaikan ini sebelum pukul delapan malam."
        n "Atasannya menyerahkan setumpuk kertas ke arah Anita."

        menu:
            "Ya":
                n "Anita menghela nafasnya pasrah."
                a "Baik, Pak."
                a "Akan saya kerjakan, Pak. Tapi, apakah saya boleh meminta uang tambahan karena saya lembur hampir setiap hari selama saya bekerja di sini, Pak?"
                an "Uang tambahan? Enak saja! Seharusnya kamu bersyukur sudah saya terima bekerja di sini di usia kamu yang sudah tua!"
                a "Tapi, Pak–"
                an "Sudah-sudah, tidak usah banyak protes. Cepat kerjakan!"
                n "Lagi-lagi Anita tidak bisa pulang tepat waktu."

            "Tidak":
                a "Maaf, Pak. Saya tidak bisa lembur hari ini."
                an "Apa?! Kamu berani menolak perintah saya?!"
                a "Saya sudah bekerja lembur hampir setiap hari, Pak. Saya butuh waktu untuk keluarga saya."
                an "Kalau begitu, kamu bisa cari pekerjaan lain!"
                n "Anita terdiam. Ia tahu bahwa mencari pekerjaan di usianya tidaklah mudah. Dengan berat hati, ia menerima tumpukan kertas itu."
                a "Baik, Pak."

        n "Setelah melewati perjalanan cukup lama, akhirnya Anita tiba di rumah."

        menu:
            "Mengunjungi kamar anak-anaknya":
                n "Tanpa berpikir panjang, kakinya ia langkahkan menuju kamar milik Dita. Ditemukannya Dita sudah tertidur pulas di atas ranjangnya."
                n "Anita kemudian melapisi tubuh putrinya dengan selimut, menjaganya tetap hangat."
                n "Berikutnya, Anita pergi ke kamar sebelah. Matanya juga menangkap badan sang pemilik terbaring di atas kasur dengan mata terpejam."
                n "Kemudian Anita mengusap lembut kepala putranya dan mengucapkan,"
                a "Terima kasih, Kak. Ibu minta maaf ya."

            "Langsung pergi ke kamarnya":
                n "Anita sudah berada di dalam kamarnya. Tas dan blazer ia taruh di salah satu sisi kasur."
                n "Kakinya ia langkahkan menuju kamar mandi untuk membersihkan diri dan mengganti pakaiannya. Sebelum pergi tidur, ia merasa haus."

        scene bg_dining_room with fade
        show anita at Transform(xpos=0.5, ypos=200, xanchor=0.5) with dissolve

        n "Kini Anita berada di dapur. Sebelum mengambil gelas dari dalam rak untuk diisi air putih, langkahnya sempat terhenti ketika melihat wastafel berisi piring dan gelas kotor."
        n "Awalnya, Anita berniat untuk mencuci piring-piring tersebut, tetapi tubuhnya terasa amat lelah. Belum lagi, ia harus kembali bekerja besok."
        n "Setelah minum, Anita akhirnya memutuskan untuk pergi tidur guna memulihkan energi."
        n "Hari demi hari berlalu, rutinitas Anita tak banyak berubah. Lembur menjadi hal yang biasa dan hak Anita untuk menerima uang tambahan dari atasannya tak pernah terealisasi."
        n "Sementara itu, di rumah, Dypho dan Dita tumbuh besar tanpa banyak merasakan kehangatan seorang ibu. Bahkan, Dita seringkali merasa kesepian dan bertanya-tanya kepada Sang Kakak mengapa Anita jarang berada di rumah."
        n "Malam ini, setibanya Anita di rumah, ia baru ingat kalau dirinya lupa meninggalkan uang makan untuk Dypho dan Dita sebab pagi tadi ia terburu-buru berangkat ke kantor dikarenakan bangun terlambat."

        a "Ya ampun, aku sampai lupa nyimpen uang buat anak-anak. Anak-anak makan ga ya hari ini?"

        n "Anita bergerak menuju dapur dan kemudian membuka kulkas. Barangkali ia bisa memasak makanan untuk anak-anaknya."
        n "Kosong. Kulkasnya tidak berisi apapun. Anita mengacak-acak rambut dan mengutuk dirinya sendiri."

        a "Anita, kamu bahkan ga pantas disebut sebagai ibu!"

        n "Tubuh Anita kini bersandar pada kulkas. Kedua lengannya memeluk lutut yang ditekuk dan kepalanya menunduk."
        n "Anita merasa kehilangan sedikit demi sedikit waktu, kesehatan, dan yang paling menyakitkan, hubungan dengan anak-anaknya."

        a "Dypho, Dita, maafkan Ibu. Maaf karena kalian mempunyai ibu yang buruk. Maaf karena Ibu belum mampu mengubah keadaan ini."

        n "•••"

        n "Keesokan harinya, Anita memutuskan untuk berbicara dengan atasannya setelah ia menyelesaikan pekerjaannya."
        n "Dengan keberanian yang besar, ia menyampaikan keluhan tentang beban kerja yang berlebihan dan haknya sebagai pekerja yang tidak dipenuhi. Namun, atasannya tetap bersikeras dan mengancam akan memecatnya jika Anita terus mengeluh."

        n "Merasa putus asa, Anita pulang ke rumah dengan perasaan campur aduk. Lagi-lagi, ia merasa gagal sebagai seorang ibu dan sebagai seorang pekerja."
        n "Setibanya di rumah dengan rasa bersalah dan gelisahnya, netranya menangkap sosok yang sudah lama hilang tengah duduk di kursi ruang tamu."

        show bapak at Transform(xpos=0.0, ypos=50, xanchor=0.0) with dissolve

        a "Baithar? Kamu beneran Baithar? Kamu masih hidup?"

        b "Iya, Anita. Aku Baithar."

        n "Seketika tangisan Anita pecah. Perasaan yang selama ini ia pendam akhirnya meluap."

        menu:
            "Memeluknya":
                a "Kedua tangan Anita ia lingkarkan ke tubuh milik Baithar."
                # play sound "sfx_tampar.mp3"                                   Kenapa masih sfx tampar? Sebaiknya delete?
                b "Sudah. Nanti pipi kamu sakit, Anita."

            "Memukulnya":
                play sound "sfx_tampar.mp3"
                a "Tangan Anita bahkan bergerak aktif memukul-mukul Sang Suami."
                # b "Sudah. Nanti pipi kamu sakit, Anita."                      Kenapa pipinya sakit?

        a "Baithar, kamu kemana selama hampir 4 tahun? Tega ya ninggalin aku sama anak-anak?"
        a "Kamu tahu kalau selama kamu pergi, Dypho sama Dita ga cuma kehilangan sosok ayah, tapi juga sosok ibu! Kamu tahu kalau aku harus pergi pagi-pagi dan pulang pas anak-anak udah tidur karena lembur?!"
        a "Kamu tahu kalau aku ga dapat gaji tambahan meskipun udah kerja sampai malam?! Kamu tahu kalau aku bahkan ga bisa jadi ibu yang kasih hak buat anak-anak terima kasih sayang aku?!"
        a "Kamu tahu kalau aku selama ini selalu dihantui rasa bersalah karena ga bisa membersamai Dypho dan Dita?!"
        
        jump epilog

    # Epilogue for both POV
    label epilog:
    scene black with fade
    play music "scene_epilog.mp3" fadeout 1
    "Epilog"
    "2020"
    
    scene bg_dining_room with fade
    show bapak at Transform(xpos=0.5, ypos=50, xanchor=0.5) with dissolve
    n "Baithar kini tengah menyantap menu makan siangnya. Tak lama, datang sosok yang sedikit lebih tinggi darinya menempati kursi yang terletak di seberang Baithar."
    n "Ernest Haryono namanya. Saat ini keduanya sedang bekerja di perusahaan yang sama, Wudden's Lab–laboratorium swasta–. Namun, mereka berada pada sub-bidang yang berbeda."
    define e = Character("Ernest", color="#FFD700")
    b "Ernest, kau tahu apa yang baru saja saya temukan?"
    e "Tidak tahu. Tapi, pasti itu memiliki hubungan dengan obat-obatan 'kan? Keahlianmu di sana."

    b "Betul."
    n "Baithar mengangguk sembari menelan makanan di mulutnya. Ia kemudian mengecilkan volume suaranya."

    b "Saya menemukan bahan yang dapat dimanfaatkan untuk membuat obat wabah penyakit yang akhir-akhir ini penyebarannya mulai meluas di kota."
    b "Meskipun sejauh ini, kemungkinan bahan tersebut aman digunakan masih terhitung kecil, hanya sekitar 37 persen."

    n "Ernest terkejut sekaligus takjub mendengarnya. Percayalah, sampai hari ini, solusi untuk penyakit tersebut belum juga ditemukan."

    b "Tapi, ini masih rahasia. Tolong jangan beritahu siapapun."

    scene black with fade
    pause 1.0

    "•••"
    n "Suara dentuman keras antara piring berbahan logam dengan lantai mengusik telinga milik Baithar sehingga mau tidak mau ia terbangun dari tidurnya."

    scene dim_room with fade
    show bapak at Transform(xpos=0.5, ypos=50, xanchor=0.5) with dissolve
    n "Saat baru membuka mata, pandangannya menatap langit-langit yang hanya dihiasi sebuah lampu berwarna kekuningan yang cukup redup. Tubuh Baithar dipaksa bangkit dari posisi berbaring."

    b "Di mana ini?"

    n "“Aku tidak butuh makan! Keluarkan aku dari sini!” ujar seseorang."

    n "Baithar terkejut dan kepalanya secara otomatis menghadap ke sumber suara. Kini, dirinya menyadari bahwa ia juga terkurung dalam sebuah jeruji besi."

    scene cell_with_baithar
    n "Dengan terburu-buru, Baithar mengangkat tubuhnya dari kasur yang beralaskan ranjang yang sudah berkarat, menuju pintu sel yang digembok."

    scene black with fade
    pause 1.0

    "•••"
    "2024"
    n "Terhitung sudah tiga setengah tahun Baithar dikurung. Ia beruntung karena masih hidup setelah melalui beragam penyiksaan. Akhirnya, setelah beribu cara ia lakukan, Baithar berhasil meloloskan dirinya dari sana."

    scene city_at_night
    n "Kini Baithar berada di pusat kota dalam kondisi memakai baju lusuh dan tubuhnya dipenuhi noda sisa-sisa dari tempat ia dikurung."

    n "Dilihatnya billboard yang menempel di gedung-gedung sedang menayangkan berita terkini mengenai penurunan jumlah penderita yang terjangkit wabah."

    show billboard_news at center
    n "Disebutkan bahwa hal tersebut dapat terjadi karena obat yang ditemukan oleh Wakil Direktur Wudden’s Lab ampuh untuk menyembuhkan penyakit tersebut."

    b "..."
    n "Meskipun diselimuti perasaan tidak terima, Baithar memutuskan melanjutkan perjalanan ke rumahnya."

    scene baithar_home with fade
    n "Hari semakin gelap. Sesampainya Baithar, ia menekan bel rumahnya."

    n "(The End)"
    return
