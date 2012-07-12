/* Belirli bir metin dosyası içerisinde yer alan metni, bazı özel karakterler (<, >)
kullanılarak normal metinden izole edilmiş etiketlerden hareketle biçimleyerek ekrana
yazdıran program */

using System;
using System.IO;

namespace Uzay2				/*namespace*/
{
    class Stack				/*class*/
    {
        public string[] dizi;
        public int sayac;
        public int boyut;

        public Stack(int uzunluk)			/*ilklendirme kismi*/
        {
            dizi = new string[uzunluk];
            sayac = 0;
            boyut = uzunluk;
        }

        public bool IsEmpty()				/*Stack'in doluluguna bakar*/
        {
            if (sayac == 0)
                return true;
            else
                return false;
        }

        public int Push(string eklenen)		/*Stack'a eleman itme*/
        {
            if (sayac < boyut)
            {
                dizi[sayac] = eklenen;
                sayac++;
                return sayac - 1;
            }
            return -1;
        }

        public string Peek()				/*Stack'in son elemanini döndürür*/
        {
            if (IsEmpty())
                return null;
            return dizi[sayac - 1];
        }

        public string Pop()					/*Stack'in son elemanini ceker*/
        {
            string son = Peek();
            if (IsEmpty())
                return null;
            dizi[sayac - 1] = "";
            sayac--;
            return son;
        }
    }/*class*/
    class Sinif1													/*class*/
    {
        public static string Oku(string DosyaAdresi)  				/*Dosyadan okuma*/
        {
            string okunan = "";
            StreamReader sr = new StreamReader(DosyaAdresi);
            okunan = sr.ReadToEnd();
            sr.Close();
            return okunan;
        }

        public static void Yaz(string DosyaAdresi, string metin)  	/*Dosyaya yazma*/
        {
            StreamWriter sw = new StreamWriter(DosyaAdresi);
            sw.Write(metin);
            sw.Close();
        }

        public static bool Tag_mi(string girdi)					    /*Tag kontrolü yapar*/
        {
            int i;
            string icerideki;

            Stack tutulacak = new Stack(girdi.Length);
            for (i = 0; i < girdi.Length; i++)
            {
                if (((girdi[i] == 'u') || (girdi[i] == 'b') || (girdi[i] == 'h') || (girdi[i] == 'p')) && (girdi[i - 1] == '<'))
                    tutulacak.Push(Convert.ToString(girdi[i]));
                if (((girdi[i] == 'u') || (girdi[i] == 'b') || (girdi[i] == 'h') || (girdi[i] == 'p')) && (girdi[i - 1] == '/'))
                {
                    icerideki = tutulacak.Pop();
                    if (icerideki != Convert.ToString(girdi[i]))
                        return false;
                }
            }
            if (tutulacak.IsEmpty())							    /*Stack te eleman kaldı mı?*/
                return true;
            else
                return false;

        }/*Tag_mi*/

        public static string Tekrarla(string al)					/*Koyu yazdirma*/
        {
            string tut = "";
            int say;
            for (say = 0; say < al.Length; say++)
                tut += (al[say] + "" + al[say]);
            return tut;
        }

        public static string Koseli(string al)						/*Koseli parantezler içinde yazma*/
        {
            string tut = "[" + al + "]";
            return tut;
        }

        public static string Gizle(string al)						/*Görünmeyecek kisim*/
        {
            return "";
        }

        public static string Buyut(string al)						/*Buyuk yazdirma*/
        {
            return al.ToUpper();
        }

        public static string Hangislem(char gorev, string kelime)  	/*Hangi islemin yapılacagi seçimi*/
        {
            if (gorev == 'b')
                return Tekrarla(kelime);
            else if (gorev == 'u')
                return Buyut(kelime);
            else if (gorev == 'p')
                return Koseli(kelime);
            else if (gorev == 'h')
                return Gizle(kelime);
            else
                return " ";
        }/*Hangislem*/

        public static string Cozumleme(string al)					/*Cözümleme yapilmasi*/
        {					
            Stack anastack = new Stack(al.Length);
            Stack gecicistack = new Stack(al.Length);

            string gorev = "", kelime = "", sonuc = "";
            bool state = false;
            int i;
            for (i = 0; i < al.Length; i++)
            {
                if (al[i] == '<')
                {
                    state = true;
                    if (kelime != "")
                    {
                        while ((gorev = anastack.Pop()) != null)
                        {
                            kelime = Hangislem(gorev[1], kelime);
                            gecicistack.Push(gorev);
                        }
                        while ((gorev = gecicistack.Pop()) != null)
                            anastack.Push(gorev);
                        sonuc += kelime;
                    }
                    kelime = "";
                    gorev += al[i];
                }
                else if (state && al[i] == '>')
                {
                    gorev += al[i];
                    if (gorev[1] == '/')
                        anastack.Pop();
                    else
                        anastack.Push(gorev);
                    gorev = "";
                    state = false;
                }
                else if (state)
                    gorev += al[i];
                else
                    kelime += al[i];
            }
            sonuc += kelime;
            return sonuc;
        }/*Cozumleme*/

        public static void Main()				/* Ana fonksiyon*/
        {

            string son;
            string okunan = Oku("C:/kaynak.txt");
            son = Cozumleme(okunan);
            if (!Tag_mi(okunan))
                Console.WriteLine("Kaynak dosyanin bicimleme etiketleri hatalidir, kontrol ediniz. ");
            else
            {
                son = Cozumleme(okunan);
                Console.WriteLine(son);
            }
            Console.ReadLine();
        } /*Main*/
    } /*class sinif1*/
}/*namespace*/
