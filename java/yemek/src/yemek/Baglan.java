package yemek;


import java.sql.*;

public class Baglan {
	private Connection _con;
	private String _dbusername = "messah"; 
	private String _dbpassword = "12345"; 
	private String _drivername = "oracle.jdbc.driver.OracleDriver";
	private String url = "jdbc:oracle:thin:@localhost:1521:xe";

	public Baglan() {
		try {
			Class.forName(_drivername).newInstance();
			setCon((Connection) DriverManager.getConnection(url, _dbusername,
					_dbpassword));
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public Connection getCon() {
		return _con;
	}

	public void setCon(Connection _con) {
		this._con = _con;
	}
}
