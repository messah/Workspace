package yemek;

import java.util.Date;

public class YemekMenu {
	private Long id;
	private Date tarih;
	private int kacinci;
	private Yemek yemek;
	private Boolean secilenSatir = false;
	private Boolean Editsec = false;

	public Boolean getEditsec() {
		return Editsec;
	}

	public void setEditsec(Boolean editsec) {
		Editsec = editsec;
	}

	public YemekMenu() {
		// TODO Auto-generated constructor stub
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public Date getTarih() {
		return tarih;
	}

	public void setTarih(Date tarih) {
		this.tarih = tarih;
	}

	public int getKacinci() {
		return kacinci;
	}

	public void setKacinci(int kacinci) {
		this.kacinci = kacinci;
	}

	public Yemek getYemek() {
		return yemek;
	}

	public void setYemek(Yemek yemek) {
		this.yemek = yemek;
	}

	public Boolean getSecilenSatir() {
		return secilenSatir;
	}

	public void setSecilenSatir(Boolean secilenSatir) {
		this.secilenSatir = secilenSatir;
	}

	// public int getKalori() {
	// return kalori;
	// }
	// public void setKalori(int kalori) {
	// this.kalori = kalori;
	// }
	// public String getTarif() {
	// return tarif;
	// }
	// public void setTarif(String tarif) {
	// this.tarif = tarif;
	// }
	// public String getYemek() {
	// return yemek;
	// }
	// public void setYemek(String yemek) {
	// this.yemek = yemek;
	// }

}
