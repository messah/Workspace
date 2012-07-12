package yemek;



public class Yemek {
	private long id;
	private String yemek;
	private int kalori;
	private String tarif;

	public Yemek() {
		// TODO Auto-generated constructor stub
	}
	public Yemek(long id, String yemek, int kalori,String tarif) {

      this.id=id;
      this.yemek=yemek;
      this.kalori=kalori;
      this.tarif=tarif;
	}
	
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public String getYemek() {
		return yemek;
	}
	public void setYemek(String yemek) {
		this.yemek = yemek;
	}
	public int getKalori() {
		return kalori;
	}
	public void setKalori(int kalori) {
		this.kalori = kalori;
	}
	public String getTarif() {
		return tarif;
	}
	public void setTarif(String tarif) {
		this.tarif = tarif;
	}
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return this.yemek;
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + (int) (id ^ (id >>> 32));
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		final Yemek other = (Yemek) obj;
		if (id != other.id)
			return false;
		return true;
	}
	

}
