package yemek;

import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.faces.component.UIComponent;
import javax.faces.context.FacesContext;
import javax.faces.convert.Converter;

public class ConverterBean implements Converter {

	public Object getAsObject(FacesContext context, UIComponent component,
			String value) {
		return objeCevir(value);
	}

	public String getAsString(FacesContext context, UIComponent component,
			Object value) {
		if (value instanceof Yemek) {
			Yemek ymk = (Yemek) value;
			return ymk.getYemek();
		}
		return "";

		// return ((YemekBean) value).getString();
	}

	PreparedStatement pst;
	Baglan baglan = new Baglan();
	private ResultSet rs;

	public Object objeCevir(String value) {
		Yemek yemek = new Yemek();
		try {
			pst = baglan.getCon().prepareStatement(
					"select id,yemek,kalori,tarif from p_yemek where yemek=?");
			pst.setString(1, value);
			rs = pst.executeQuery();

			while (rs.next()) {
				yemek.setId(rs.getLong("id"));
				yemek.setYemek(rs.getString("yemek"));
				yemek.setKalori(rs.getInt("kalori"));
				yemek.setTarif(rs.getString("tarif"));
			}
		} catch (Exception e) {
			System.out.println(e);
		}
		return yemek;

	}
}
