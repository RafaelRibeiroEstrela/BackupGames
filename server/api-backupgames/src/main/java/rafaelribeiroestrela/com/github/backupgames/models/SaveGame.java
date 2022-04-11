package rafaelribeiroestrela.com.github.backupgames.models;

import java.time.LocalDate;
import java.util.Objects;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Entity
@Table(name = "TB_SAVEGAME")
public class SaveGame {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "ID_SAVEGAME")
	private Long id;
	
	@Column(name = "SAVE_DATE")
	private LocalDate date;
	
	@Column(name = "ARRAY_BYTES")
	private byte[] bytes;
	
	@ManyToOne
	@JoinColumn(name = "ID_GAME")
	private Game game;
	
	public SaveGame() {
		
	}

	public SaveGame(Long id, LocalDate date, byte[] bytes, Game game) {
		super();
		this.id = id;
		this.date = date;
		this.bytes = bytes;
		this.game = game;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public LocalDate getDate() {
		return date;
	}

	public void setDate(LocalDate date) {
		this.date = date;
	}

	public byte[] getBytes() {
		return bytes;
	}

	public void setBytes(byte[] bytes) {
		this.bytes = bytes;
	}

	public Game getGame() {
		return game;
	}

	public void setGame(Game game) {
		this.game = game;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		SaveGame other = (SaveGame) obj;
		return Objects.equals(id, other.id);
	}
	
	

}
