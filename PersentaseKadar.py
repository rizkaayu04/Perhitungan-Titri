import streamlit as st 


# Menampilkan judul dengan warna merah
st.markdown("<h1 style='color: deepskyblue;'>STANDARDISASI DAN PENETAPAN KADAR MENURUT MATA KULIAH ANALISIS TITRIMETRI</h1>", unsafe_allow_html=True)

#Tampilkan konten terkait dengan menu yang dipilih
def halaman_utama():
    #Konten untuk HALAMAN UTAMA
    st.header('Kalkulator Perhitungan Standardisasi dan Penetapan Kadar',divider='rainbow')
    st.markdown('<span style="color:pink">Hello Teman-teman! :balloon:</span>', unsafe_allow_html=True)
    st.markdown('<span style="color:pink">Belajar kimia bersama Gerhat</span>', unsafe_allow_html=True)
    st.markdown('<span style="color:pink">Selamat datang di Kalkulator Kelompok 4</span>', unsafe_allow_html=True)
    st.write('---')
    st.write('Kelompok 4')
    st.write('1. Destiana Diah Ayu Safitri (2360100)')
    st.write('2. Gerhat Karol Sardo Jonathan Sitorus (2360131)')
    st.write('3. Rachel Tabita Gabe Sitorus (2360227)')
    st.write('4. Rizka Ayu Putri Aulia (2360245)')
    st.write('5. Shabiyyah Ayu Nailah Sekar (2360259)')
    


#Membuat sidebar menu
menu_options=["HALAMAN UTAMA","INFORMASI","STANDARDISASI","PENETAPAN KADAR"]
selected_menu=st.sidebar.radio("Menu",menu_options)

#Tampilan kalkulator yang dipilih
if selected_menu == "HALAMAN UTAMA":
    halaman_utama()


if selected_menu == "STANDARDISASI":
    STANDARDISASI1, STANDARDISASI2, STANDARDISASI3, STANDARDISASI4, STANDARDISASI5 = st.tabs(['Standardisasi Larutan Basa','Standardisasi Larutan Asam','Standardisasi Larutan KMno4','Standardisasi Tiosulfat','Standardisasi Larutan EDTA' ])
    
    with STANDARDISASI1:
        st.subheader ("Standardisasi Larutan Basa", divider='violet')
        st.write('<span style="color:red">Bobot Molekul Asam Oksalat (C₂H₂O₄.2H₂O) adalah 126 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('C₂H₂O₄ + 2NaOH → Na₂C₂O₄ + 2H₂O ')
        st.latex(r'''Normalitas NaOH =\frac{mg Asam Oksalat}{100/25 x mL NaOH x BE Asam Oksalat}''')
        st.write('---')

        bobot = st.number_input('Masukkan bobot Asam Oksalat (mg)')
        st.write('bobot Asam Oksalat adalah', bobot)

        titran = st.number_input('Masukkan volume NaOH (mL)')
        st.write('volume NaOH adalah', titran)

        ekivalen = st.number_input('Masukkan nilai BE(mg⁄mgrek)')
        st.write('bobot ekivalen Asam Oksalat adalah', ekivalen)

        if st.button('Hitung Normalitas NaOH dalam standardisasi Basa dengan sampel Asam Oksalat'):
            persentase = (bobot / (4 * titran * ekivalen) )
            persentase_formatted = "{:.4f}".format(persentase)
            st.write(f'Nilai Normalitas NaOH dalam Asam Oksalat adalah = {persentase_formatted} N')

    with STANDARDISASI2:
        st.subheader ("Standardisasi Larutan Asam",divider='violet')
        st.write('<span style="color:red">Bobot Molekul Boraks (Na₂B₄O₇.10H₂O) adalah 381.4 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('Na₂B₄O₇.10H₂O + 2HCl → 2NaCl + 4H₃BO₃ +5H₂O ')
        st.latex(r'''Normalitas HCl =\frac{mg boraks}{100/25 x mL HCl x BE Boraks}''')
        st.write('---')
        bobot = st.number_input('Masukkan bobot Boraks (mg)')
        st.write('bobot Boraks adalah', bobot)

        titran = st.number_input('Masukkan volume HCl (mL)')
        st.write('volume HCl adalah', titran)

        ekivalen = st.number_input('Masukkan nilai BE Boraks (mg⁄mgrek)')
        st.write('bobot ekivalen Boraks adalah', ekivalen)

        if st.button('Hitung Normalitas HCl dalam standardisasi Asam dengan sampel Boraks'):
            persentase = (bobot / (4 * titran * ekivalen))
            persentase_formatted = "{:.4f}".format(persentase)
            st.write(f'Nilai Normalitas HCl dalam Boraks adalah = {persentase_formatted} N')

    with STANDARDISASI3:
        st.subheader ("Standardisasi Larutan KMnO₄ dengan Asam Oksalat",divider='violet')
        st.write('<span style="color:red">Bobot Molekul Asam Oksalat (C₂H₂O₄.2H₂O) adalah 126 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('MnO4− + 5C₂H₂O₄ + 6H⁺ → 2Mn²⁺ + 10CO₂ + 8H₂O')
        st.latex(r'''Normalitas KMnO₄ =\frac{mg Asam Oksalat}{100/25 x mL KMnO₄ x BE Asam Oksalat}''')
        st.write('---')

        bobot = st.number_input('Masukkan bobot asam oksalat (mg)')
        st.write('bobot Asam Oksalat adalah', bobot)

        titran = st.number_input('Masukkan volume KMnO₄ (mL)')
        st.write('volume KMnO₄ adalah', titran)

        ekivalen = st.number_input('Masukkan nilai BE asam oksalat (mg⁄mgrek)')
        st.write('bobot ekivalen Asam Oksalat adalah', ekivalen)

        if st.button('Hitung Normalitas KMnO₄ dalam standardisasi larutan KMnO₄ dengan Asam Oksalat'):
            persentase = (bobot / (4 * titran * ekivalen))
            persentase_formatted = "{:.4f}".format(persentase)
            st.write(f'Nilai Normalitas KMnO₄ dalam Asam OksalaT adalah = {persentase_formatted} N')

    with STANDARDISASI4:
        st.subheader ("Standardisasi Larutan Tiosulfat 0,1 N dengan Bikromat secara Iodometri",divider='violet')
        st.write('<span style="color:red">Bobot Molekul Kalium Dikromat (K₂Cr₂O₇) adalah 294 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('K₂Cr₂O₇ + 6KI + 14HCl → 8KCl + 2CrCl₃ + 7H₂O + 3I₂')
        st.write('Na₂S₂O₃ + I₂ → Na₂S₄O₆ + 2NaI')
        st.latex(r'''Normalitas Na₂S₂O₃ =\frac{mg K₂Cr₂O₇}{100/25 x mL Tio x BE K₂Cr₂O₇}''')
        st.write('---')

        bobot = st.number_input('Masukkan bobot K₂Cr₂O₇ (mg)')
        st.write('bobot K₂Cr₂O₇ adalah', bobot)

        titran = st.number_input('Masukkan volume Tio (mL)')
        st.write('volume Tio adalah', titran)

        ekivalen = st.number_input('Masukkan nilai BE K₂Cr₂O₇ (mg⁄mgrek)')
        st.write('bobot ekivalen K₂Cr₂O₇ adalah', ekivalen)

        if st.button('Hitung Normalitas Na₂S₂O₃ dalam standardisasi larutan Tio 0,1 N dengan K₂Cr₂O₇'):
            persentase = (bobot / (4 * titran * ekivalen))
            persentase_formatted = "{:.4f}".format(persentase)
            st.write(f'Nilai Normalitas Na₂S₂O₃ dalam larutan Tio 0,1 N dengan K₂Cr₂O₇ adalah = {persentase_formatted} N')

    with STANDARDISASI5:
        st.subheader ("Standardisasi larutan EDTA 0,01 M dengan CaCO₃",divider='violet')
        st.write('<span style="color:red">Bobot Molekul Kalsium Karbonat (CaCO₃) adalah 100 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('Mg²⁺ + HIn²⁻ → MgIn⁻ + H⁺')
        st.write('Ca²⁺ + H₂Y²⁻ → CaY²⁻ + 2H⁺')
        st.write('MgIn⁻ + H₂Y²⁻ → MgY²⁻ + HIn²⁻ + H⁺')
        st.latex(r'''Molaritas EDTA =\frac{mg CaCO₃}{100/25 x mL EDTA x BE CaCO₃}''')
        st.write('---')

        bobot = st.number_input('Masukkan bobot CaCO₃ (mg)')
        st.write('bobot CaCO₃ adalah', bobot)

        titran = st.number_input('Masukkan volume EDTA (mL)')
        st.write('volume EDTA adalah', titran)

        ekivalen = st.number_input('Masukkan nilai BM CaCO₃ (mg⁄mmol)')
        st.write('bobot molekul CaCO₃ adalah', ekivalen)

        if st.button('Hitung Molaritas EDTA dalam standardisasi larutan EDTA 0,01 M dengan CaCO₃'):
            persentase = (bobot / (4 * titran * ekivalen))
            persentase_formatted = "{:.4f}".format(persentase)
            st.write(f'Nilai Molaritas EDTA dalam larutan EDTA 0,01 M dengan CaCO₃ adalah = {persentase_formatted} N')


if selected_menu == "PENETAPAN KADAR":
    KADAR1, KADAR2, KADAR3, KADAR4, KADAR5, KADAR6 = st.tabs(['Penetapan Kadar CH₃COOH','Penetapan Kadar NaOH dan Na₂CO₃','Penetapan Kadar Fe','Penetapan kadar Cl','Penetapan Kadar Cl','Penetapan Kesadahan' ])

    with KADAR1:
        st.subheader ("Penetapan Kadar Asam Asetat dalam cuka makan", divider='violet')
        st.write('<span style="color:red">Bobot Molekul Asam Asetat (CH₃COOH) adalah 60 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('CH₃COOH + NaOH → CH₃COONa + H₂O')
        st.write('---')

        titran = st.number_input('Masukkan volume NaOH  (mL)')
        st.write('Volume NaOH adalah', titran)

        Normalitas = st.number_input('Masukkan Normalitas NaOH (mgrek⁄mL)')
        st.write('Normalitas NaOH adalah', Normalitas)

        ekivalen = st.number_input('Masukkan nilai BE CH₃COOH (mg⁄mgrek)')
        st.write('Bobot ekivalen CH₃COOH adalah', ekivalen)

        titrat =  st.number_input('Masukkan volume sampel  (mL)')
        st.write('Volume sampel adalah', titrat)

        if st.button('Hitung Kadar Asam Asetat dalam Cuka Makan'):
            persentase = (((titran * Normalitas * ekivalen * 0.001) / titrat) * 50 * 100 )
            persentase_formatted = "{:.2f}".format(persentase)
            st.write(f'Nilai Persentase Kadar Asam Asetat dalam Cuka Makan adalah = {persentase_formatted} % (b/v)')

    with KADAR2:
        st.subheader ("Penetapan Kadar  NaOH dan Na₂CO₃ dalam Campuran Secara (WARDER) secara asidimetri", divider='violet')
        st.write('<span style="color:red">Bobot Molekul Natrium Hidroksida (NaOH) adalah 40 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('<span style="color:red">Bobot Molekul Natrium Karbonat (Na₂CO₃) adalah 106 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('NaOH + HCl → NaCl + H₂O')
        st.write('Na₂CO₃ + HCl → NaHCO₃ + NaCl')
        st.write('NaHCO₃ + HCl → NaCl + H₂CO₃ ')
        st.write('---')

        titrana = st.number_input('Masukkan volume HCl dengan indikator PP (mL)')
        st.write('Volume HCl dengan indikator PP adalah', titrana)
    
        titranb = st.number_input('Masukkan volume HCl dengan indikator SM (mL)')
        st.write('Volume HCl dengan indikator SM adalah', titranb)

        Normalitas = st.number_input('Masukkan Normalitas HCl (mgrek⁄mL)')
        st.write('Normalitas HCl adalah', Normalitas)

        ekivalen = st.number_input('Masukkan nilai BE NaOH (mg⁄mgrek)')
        st.write('Bobot ekivalen NaOH adalah', ekivalen)
    
        eki = st.number_input('Masukkan nilai BE Na₂CO₃ (mg⁄mgrek)')
        st.write('Bobot ekivalen Na₂CO₃ adalah', eki)

        titrat = st.number_input('Masukkan volume Sampel  (mL)')
        st.write('Volume sampel adalah', titrat)

        if st.button('Hitung Kadar Na₂CO₃ dalam campuran (WARDER)'):
            persentase = ((( (2 * ( titranb - titrana)) * Normalitas * eki * 0.001) / titrat) * 100 )
            persentase_formatted = "{:.2f}".format(persentase)
            st.write(f'Nilai Persentase Kadar Na₂CO₃ dalam Campuran (WARDER) secara asidimetri adalah = {persentase_formatted} % (b/v)')

        if st.button('Hitung Kadar NaOH dalam campuran (WARDER)'):
            persentase = ((( ((2 * titrana) - titranb) * Normalitas * ekivalen * 0.001) / titrat) * 100 )
            persentase_formatted = "{:.2f}".format(persentase)
            st.write(f'Nilai Persentase Kadar NaOH dalam Campuran (WARDER) secara asidimetri adalah = {persentase_formatted} % (b/v)')

    with KADAR3:
        st.subheader ("Penetapan Kadar Besi dalam Sampel Garam Besi secara Permanganometri", divider='violet')
        st.write('<span style="color:red">Bobot Molekul Besi (Fe) adalah 56 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('MnO4− + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O')
        st.write('---')

        titran = st.number_input('Masukkan volume KMnO₄ (mL)')
        st.write('Volume KMnO₄ adalah', titran)

        Normalitas = st.number_input('Masukkan Normalitas KMnO₄ (mgrek⁄mL)')
        st.write('Normalitas KMnO₄ adalah', Normalitas)

        ekivalen = st.number_input('Masukkan nilai BE Fe (mg⁄mgrek)')
        st.write('Bobot ekivalen Fe adalah', ekivalen)

        titrat = st.number_input('Masukkan volume sampel garam besi (mL)')
        st.write('Volume sampel adalah', titrat)

        if st.button('Hitung Kadar Besi dalam Sampel Garam Besi'):
            persentase = (((titran * Normalitas * ekivalen * 0.001) / titrat) * 100 )
            persentase_formatted = "{:.2f}".format(persentase)
            st.write(f'Nilai Persentase Kadar Besi dalam Sampel Garam Besi adalah = {persentase_formatted} % (b/v)')

    with KADAR4:
        st.subheader ("Penetapan Kadar Klor dalam Bahan Pemutih secara Iodometri", divider='violet')
        st.write('<span style="color:red">Bobot Molekul Klorida (Cl) adalah 35,45 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi:')
        st.write('Ca(OCl)₂ + 2H₂SO₄ + 4KI → CaSO₄ + 2KCl + 2H₂O + 2I₂ + 2K₂SO₄')
        st.write('I₂ + 2Na₂S₂O₃ → 2NaI + Na₂S₄O₆ ')
        st.write('---')

        titran = st.number_input('Masukkan volume Tio (mL)')
        st.write('Volume Tio adalah', titran)

        Normalitas = st.number_input('Masukkan Normalitas Tio (mgrek⁄mL)')
        st.write('Normalitas Tio adalah', Normalitas)

        ekivalen = st.number_input('Masukkan nilai BE Cl (mg⁄mgrek)')
        st.write('Bobot ekivalen Cl adalah', ekivalen)

        titrat = st.number_input('Masukkan volume sampel pemutih (mL)')
        st.write('Volume sampel adalah', titrat)

        if st.button('Hitung Penetapan Kadar Klor dalam Bahan Pemutih'):
            persentase = (((titran * Normalitas * ekivalen * 0.001) / titrat) * 20 * 100 )
            persentase_formatted = "{:.2f}".format(persentase)
            st.write(f'Nilai Persentase Kadar Klor dalam Bahan Pemutih secara Iodometri adalah = {persentase_formatted} % (b/v)')

    with KADAR5:
        st.subheader ("Penetapan Kadar Klor secara Argentometri", divider='violet')
        st.write('<span style="color:red">Bobot Molekul Klorida (Cl) adalah 35,45 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('Reaksi yang terjadi melalui cara mohr:')
        st.write('Ag⁺ + Cl− →  AgCl')
        st.write('2Ag⁺ + CrO₄− →  Ag₂CrO₄')
        st.write('---')
        st.write('Reaksi yang terjadi melalui cara fayans:')
        st.write('Ag⁺ + Cl− →  AgCl')
        st.write('AgCl + Ag⁺ → AgCl-Ag⁺ ')
        st.write('AgCl-Ag⁺ + Fe− → AgCl-Ag⁺-Fe− ')
        st.write('---')
        
        titran = st.number_input('Masukkan volume  AgNO₃ (mL)')
        st.write('Volume  AgNO₃ adalah', titran)

        Normalitas = st.number_input('Masukkan Normalitas  AgNO₃ (mgrek⁄mL)')
        st.write('Normalitas  AgNO₃ adalah', Normalitas)

        eki = st.number_input('Masukkan nilai Bobot Ekivaelen Cl  (mg⁄mgrek)')
        st.write('Bobot ekivalen Cl adalah', eki)

        titrat = st.number_input('Masukkan volume sampel yang mengandung Cl (mL)')
        st.write('Volume sampel adalah', titrat)

        if st.button('Hitung Penetapan Kadar Klor dalam Sampel yang mengandung Cl'):
            persentase = (((titran * Normalitas * eki * 0.001) / titrat) * 100 )
            persentase_formatted = "{:.2f}".format(persentase)
            st.write(f'Nilai Persentase Kadar Klor secara Argentometri = {persentase_formatted} % (b/v)')

    with KADAR6:
        st.subheader ("Penetapan Kesadahan Jumlah dalam Sampel Air secara Kompleksometri EDTA", divider='violet')
        st.write('<span style="color:red">Bobot Molekul Kalsium Karbonat (CaCO₃) adalah 100 mg⁄mmol</span>', unsafe_allow_html=True)
        st.write('---')

        titran = st.number_input('Masukkan volume EDTA (mL)')
        st.write('Volume EDTA adalah', titran)

        Normalitas = st.number_input('Masukkan Molaritas EDTA (mmol⁄mL)')
        st.write('Molaritas EDTA adalah', Normalitas)

        ekivalen = st.number_input('Masukkan nilai BM CaCO₃ (mg⁄mmol)')
        st.write('Bobot molekul CaCO₃ adalah', ekivalen)

        titrat = st.number_input('Masukkan volume sampel air (mL)')
        st.write('Volume sampel adalah', titrat)

        if st.button('Hitung Penetapan Kesadahan Jumlah dalam Sampel Air'):
            persentase = (((titran * Normalitas * ekivalen ) / titrat))
            persentase_formatted = "{:.2f}".format(persentase)
            st.write(f'Nilai  Kesadahan Jumlah dalam Sampel Air secara Kompleksometri EDTA adalah = {persentase_formatted} % (b/v)')


#Tampilan Bagian Informasi
if selected_menu == "INFORMASI":
    INFO1, INFO2 = st.tabs(['Standardisasi','Penetepan Kadar'])

    with INFO1 :
        st.subheader('Standardisasi')
        st.write('Standardisasi adalah proses pembentukan standar teknis, standardisasi spesifikasi, standar cara uji, standar definisi, prosedur standar (atau praktik), dan lain-lain. Dapat disimpulkan standardisasi pada suatu produk ialah penetapan mutu yang selanjutnya menjadi pedoman untuk terpenuhinya keselarasan kuantitas yang menjamin kualitas produk.')
        ar_option = st.selectbox ('Pilih Jenis Standardisasi', ['None','Standardisasi Larutan Asam','Standardisasi Larutan Basa','Standardisasi Larutan KMnO₄','Standardisasi Larutan Tiosulfat','Standardisasi Larutan EDTA'])

        if ar_option == 'Standardisasi Larutan Asam' :
            st.write('Pada standardisasi Larutan Asam (HCl 0.1 N) Sampel yang digunakan adalah Boraks dan titran adalah HCl')
            st.write('Bobot Molekul Boraks (Na₂B₄O₇.10H₂O) adalah 381.4 mg⁄mmol')
            st.write('Titrasi pada standardisasi larutan asam (HCl) menggunakan indikator Metil Merah (MM) sebanyak 2 tetes')
            st.write('Perubahan warna yang terjadi yaitu "larutan berwarna kuning → larutan berwarna merah jingga" ')

        if ar_option == 'Standardisasi Larutan Basa' :
            st.write('Pada standardisasi Larutan Basa (NaOH 0.1 N). Sampel yang digunakan adalah Asam Oksalat dan titran adalah NaOH')
            st.write('Bobot Molekul Asam Oksalat (C₂H₂O₄.2H₂O) adalah 126 mg⁄mmol')
            st.write('Titrasi pada standardisasi larutan basa (NaOH) menggunakan indikator Fenolftalein (PP) sebanyak 1 tetes')
            st.write('Perubahan warna yang terjadi yaitu "larutan tidak berwarna → larutan berwarna merah muda seulas" ')
            
        if ar_option == 'Standardisasi Larutan KMnO₄' :
            st.write('Pada standardisasi Larutan KMnO₄ 0.1 N. Sampel yang digunakan adalah Asam Oksalat dan titran adalah KMnO₄')
            st.write('Bobot Molekul Asam Oksalat (C₂H₂O₄.2H₂O) adalah 126 mg⁄mmol')
            st.write('Titrasi pada standardisasi larutan  KMnO₄ tidak menggunakan indikator karena  KMnO₄ dapat menjadi auto indikator')
            st.write('Perubahan warna yang terjadi yaitu "Larutan tidak berwarna → Larutan berwarna merah muda seulas" ')

        if ar_option == 'Standardisasi Larutan Tiosulfat' :
            st.write('Pada standardisasi Larutan Tiosulfat 0.1 N. Sampel yang digunakan adalah Kalium Dikromat (K₂Cr₂O₇) dan titran adalah larutan Tio')
            st.write('Bobot Molekul Kalium Dikromat (K₂Cr₂O₇) adalah 294 mg⁄mmol ')
            st.write('Titrasi pada standardisasi larutan tiosulfat menggunakan indikator KI - Kanji')
            st.write('KI diberi sebanyak 10 mL sebelum dilakukan titrasi')
            st.write('Perubahan warna yang terjadi yaitu "Larutan berwarna coklat → Larutan berwarna kuning-hijau" ')
            st.write('Setelah mencapai warna antara kuning-hijau, diberi indikator kanji sebanyak 1 drop')
            st.write('Perubahan warna yang terjadi yaitu "Larutan berwarna biru-ungu → Larutan berwarna hijau" ')

        if ar_option == 'Standardisasi Larutan EDTA' :
            st.write('Pada standardisasi Larutan EDTA 0.01 M. Sampel yang digunakan adalah Kalsium Karbonat (CaCO₃) dan titran adalah larutan EDTA')
            st.write('Bobot Molekul Kalsium Karbonat (CaCO₃) adalah 100 mg⁄mmol ')
            st.write('Titrasi pada standardisasi larutan EDTA menggunakan indikator Erio-black-T sedikit')
            st.write('Perubahan warna yang terjadi yaitu "larutan berwarna merah anggur → larutan berwarna biru" ')

    with INFO2 :
        st.subheader('Penetapan Kadar')
        st.write('Penetapan Kadar larutan adalah suatu pengukuran kandungan larutan yang berada di dalam bahan (sampel). Prinsip penetapan kadar dilakukan dengan cara yang tepat, seperti titrasi. Tujuan dari penetapan kadar larutan, yaitu memberikan batas minimal atau rentang besarnya kandungan larutan di dalam bahan.')
        warna_option = st.selectbox ('Pilih Jenis Titrasi', ['None','Penetapan Kadar Asam Asetat','Penetapan Kadar NaOH dan Na₂CO₃','Penetapan Kadar Besi','Penetapan Kadar Klor secara Iodometri','Penetapan Kadar Klor secara Argentometri','Penetapan Kesadahan' ])

        if warna_option == 'Penetapan Kadar Asam Asetat' :
            st.write('Pada Penetapan Kadar Asam Asetat, digunakan sampel Cuka Makan sebanyak 25 mL dengan titran larutan NaOH')
            st.write('Bobot Molekul Asam Asetat (CH₃COOH) adalah 60 mg⁄mmol ')
            st.write('Titrasi pada penetapan kadar asam asetat menggunakan indikator Fenolftalein (PP) sebanyak 1 tetes')
            st.write('Perubahan warna yang terjadi yaitu "larutan tidak berwarna → larutan berwarna merah muda seulas" ')

        if warna_option == 'Penetapan Kadar NaOH dan Na₂CO₃' :
            st.write('Pada Penetapan Kadar NaOH dan Na₂CO₃, digunakan sampel WARDER sebanyak 25 mL dengan titran larutan HCl')
            st.write('Bobot Molekul Natrium Hidroksida (NaOH) adalah 40 mg⁄mmol ')
            st.write('Bobot Molekul Natrium Karbonat (Na₂CO₃) adalah 106 mg⁄mmol ')
            st.write('Titrasi pada penetapan kadar NaOH dan Na₂CO₃ menggunakan 2 indikator Fenolftalein (PP) dan Sindur Metil (SM)')
            st.write('Indikator PP diberi sebanyak 1 tetes dan dilakukan titrasi sampai mengalami perubahan warna')
            st.write('Perubahan warna yang terjadi yaitu "larutan berwarna merah muda seulas → larutan tidak berwarna" ')
            st.write('Indikator SM ditambahkan sebanyak 2 tetes, apabila larutan sudah tidak berwarna')
            st.write('Perubahan warna yang terjadi yaitu "Larutan berwarna merah → Larutan berwarna kuning" ')

        if warna_option == 'Penetapan Kadar Besi' :
            st.write('Pada Penetapan Kadar Besi, digunakan sampel Garam Besi sebanyak 25 mL dengan titran larutan KMnO₄')
            st.write('Bobot Molekul Besi (Fe) adalah 56 mg⁄mmol ')
            st.write('Titrasi pada penetapan kadar besi tidak menggunakan indikator karena KMnO₄ dapat menjadi auto indikator')
            st.write('Perubahan warna yang terjadi yaitu "Larutan tidak berwarna → Larutan berwarna merah muda seulas" ')

        if warna_option == 'Penetapan Kadar Klor secara Iodometri' :
            st.write('Pada Penetapan Kadar Klor secara Iodometri, digunakan sampel Pemutih sebanyak 25 mL dengan titran larutan Tio')
            st.write('Bobot Molekul Klorida (Cl) adalah 35,45 mg⁄mmol ')
            st.write('Titrasi pada penetapan kadar klor secara iodometri menggunakan indikator KI - Kanji')
            st.write('KI diberi sebanyak 10 mL sebelum dilakukan titrasi')
            st.write('Perubahan warna yang terjadi yaitu "Larutan berwarna coklat → Larutan berwarna hijau-kuning" ')
            st.write('Setelah mencapai warna antara kuning-hijau, diberi indikator kanji sebanyak 1 drop')
            st.write('Perubahan warna yang terjadi yaitu "Larutan berwarna biru tua → Larutan tidak berwarna" ')

        if warna_option == 'Penetapan Kadar Klor secara Argentometri' :
            st.write('Pada Penetapan Kadar Klor secara Argentometri, digunakan sampel mengandung Cl sebanyak 10 mL dengan titran larutan AgNO₃ ')
            st.write('Bobot Molekul Klorida (Cl) adalah 35,45 mg⁄mmol ')
            st.write('Titrasi pada penetapan kadar klor secara argentometri dengan cara mohr menggunakan indikator K₂Cr₂O₄ sebanyak 5 tetes')
            st.write('Perubahan warna yang terjadi yaitu "Larutan berwarna kuning → Endapan merah bata" ')
            st.write('Titrasi pada penetapan kadar klor secara argentometri dengan cara fayans menggunakan indikator fluoresceion sebanyak 1-3 tetes')
            st.write('Perubahan warna yang terjadi yaitu "Larutan berwarna hijau kekuningan → Endapan berwarna merah muda" ')

        if warna_option == 'Penetapan Kesadahan' :
            st.write('Pada Penetapan Kesadahan jumlah, digunakan sampel Air sebanyak 50 mL dengan titran larutan EDTA ')
            st.write('Bobot Molekul Kalsium Karbonat (CaCO₃) adalah 100 mg⁄mmol ')
            st.write('Titrasi pada penetapan kesadahan jumlah dalam sampel air menggunakan indikator Erio-black-T sedikit')
            st.write('Perubahan warna yang terjadi yaitu "larutan berwarna merah anggur → larutan berwarna biru" ')






        

        

        
            
    

    

    
