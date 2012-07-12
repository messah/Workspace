package yemek;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import javax.faces.event.ActionEvent;
import javax.faces.event.ValueChangeEvent;
import javax.faces.model.SelectItem;

import com.icesoft.faces.component.ext.HtmlDataTable;

public class YemekBean {
	private Statement st;
	private ResultSet rs;
	PreparedStatement pst;
	String string = new String();
	Baglan nesne = new Baglan();
	List<SelectItem> yemekList = new ArrayList<SelectItem>();
	private int kalori;
	private boolean edit = false;

	private List<YemekMenu> liste = new ArrayList<YemekMenu>();

	private List<YemekMenu> listeee = new ArrayList<YemekMenu>();

	private HtmlDataTable dataTable;

	public List<YemekMenu> getListeee() {
		
	
			try {
				st = nesne.getCon().createStatement();
				rs = st
						.executeQuery("select menu.id as menuid,yemek.id as yemekid, yemek.yemek 	 as yemekadi, yemek.kalori, yemek.tarif, menu.kacinci, menu.tarih from 	 ymk_menu menu, p_yemek yemek where yemek.id=menu.yemek");

				while (rs.next()) {
					YemekMenu yemekMenu = new YemekMenu();
					Yemek yemek = new Yemek();
					yemekMenu.setYemek(yemek);
					yemekMenu.setId(rs.getLong("menuid"));
					yemekMenu.setKacinci(rs.getInt("kacinci"));
					yemekMenu.getYemek().setId(rs.getLong("yemekid"));
					yemekMenu.getYemek().setYemek(rs.getString("yemekadi"));
					yemekMenu.getYemek().setKalori(rs.getInt("kalori"));
					yemekMenu.getYemek().setTarif(rs.getString("tarif"));
					yemekMenu.setTarih(rs.getDate("tarih"));
					listeee.add(yemekMenu);
				}
			} catch (Exception e) {
				System.err.println(e);
			}
		
		return listeee;
	}


	public void kaydet(ActionEvent a) {
		System.out.println("girdi");
		int i = 0;
		getListeee();// Aslinda kullanmamaliyiz ama simdilik id yi artirmak icin kullandim
	                 
		YemekMenu yemekmenu = (YemekMenu) dataTable.getRowData();
		yemekmenu.setSecilenSatir(false);
		yemekmenu.setEditsec(false);
		

		try {
			pst = nesne.getCon().prepareStatement(
					"insert into ymk_menu (id,yemek,kacinci)  values(?,?,?)");
			pst.setLong(1, listeee.size()+1);// YANLIS !!! ID YI NASIL ATAYACAGIMIZI BILMIYORUZ...
			pst.setLong(2, yemekmenu.getYemek().getId());
			pst.setInt(3,listeee.size()+1);
			i = pst.executeUpdate();

		} catch (Exception e) {
			// TODO: handle exception
		}

		if (i > 0) {

			System.out.println("Kayit Eklendi.");

		} else
			System.out.println("sdfghjkl");
	

	}

	public void kayitSil(ActionEvent a) {

		int i = 0;
		System.out.println("Burdayim ValueChangeEvent");
		YemekMenu yemekMenu = (YemekMenu) dataTable.getRowData();

		try {
			pst = nesne.getCon().prepareStatement(
					"delete from ymk_menu where yemek=?");
			pst.setLong(1, yemekMenu.getYemek().getId());
			i = pst.executeUpdate();

			if (i > 0) {
				System.out.println(yemekMenu.getYemek().getYemek()
						+ " silindi! ");
			}

		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	private int selectedComponent = 1;

	public List<SelectItem> getYemekList() {

		if ((yemekList == null) || (yemekList.size() == 0)) {
			yemekList.add(new SelectItem(0, "Se�iniz"));
			try {
				st = nesne.getCon().createStatement();
				rs = st.executeQuery("select * from P_YEMEK");

				while (rs.next()) {
					Yemek yemekkk = new Yemek();
					yemekkk.setId(rs.getInt(1));
					yemekkk.setYemek(rs.getString(2));
					yemekkk.setKalori(rs.getInt(3));
					yemekkk.setTarif(rs.getString(4));
					yemekList.add(new SelectItem(yemekkk, yemekkk.getYemek()));
				}
				rs.close();
				st.close();

			} catch (Exception e) {
				System.out.println(e.getMessage());
			}
		}
		return yemekList;
	}

	public void checkKalori(ValueChangeEvent changeEvent) {
		System.out.println("Burdayim ValueChangeEvent");
		Yemek yemek = (Yemek) changeEvent.getNewValue();
		System.out.println("Yemek: " + yemek);
	}

	public String sec(ActionEvent a) {

		System.out.println("Burdayim sec");
		YemekMenu yemekMenu = (YemekMenu) dataTable.getRowData();
		yemekMenu.setSecilenSatir(true);
		yemekMenu.setEditsec(true);

		System.out.println(yemekMenu.getSecilenSatir());
		return null;
	}

	public void dene() {
		liste.add(new YemekMenu());
		edit = true;

	}

	public void setYemekList(List<SelectItem> yemekList) {
		this.yemekList = yemekList;
	}

	public int getKalori() {
		return kalori;
	}

	public void setKalori(int kalori) {
		this.kalori = kalori;
	}

	public Statement getSt() {
		return st;
	}

	public void setSt(Statement st) {
		this.st = st;
	}

	public ResultSet getRs() {
		return rs;
	}

	public void setRs(ResultSet rs) {
		this.rs = rs;
	}

	public PreparedStatement getPst() {
		return pst;
	}

	public void setPst(PreparedStatement pst) {
		this.pst = pst;
	}

	public Baglan getNesne() {
		return nesne;
	}

	public void setNesne(Baglan nesne) {
		this.nesne = nesne;
	}

	public int getSelectedComponent() {
		return selectedComponent;
	}

	public void setSelectedComponent(int selectedComponent) {
		this.selectedComponent = selectedComponent;
	}

	public String getString() {
		return string;
	}

	public void setString(String string) {
		this.string = string;
	}

	public boolean isEdit() {
		return edit;
	}

	public void setEdit(boolean edit) {
		this.edit = edit;
	}

	public void setListe(List<YemekMenu> liste) {
		this.liste = liste;
	}

	public HtmlDataTable getDataTable() {
		return dataTable;
	}

	public void setDataTable(HtmlDataTable dataTable) {
		this.dataTable = dataTable;
	}

	public void setListeee(List<YemekMenu> listeee) {
		this.listeee = listeee;
	}


	public List<YemekMenu> getListe() {
		return liste;
	}

}
