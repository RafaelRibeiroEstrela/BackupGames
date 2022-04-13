package rafaelribeiroestrela.com.github.backupgames.models;

import java.time.LocalDateTime;
import java.util.Objects;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

import com.fasterxml.jackson.annotation.JsonFormat;

@Entity
@Table(name = "TB_SAVEGAME")
public class Savegame {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "ID_SAVEGAME")
	private Long id;
	
	@JsonFormat(pattern = "dd/MM/yyyy HH:mm:ss")
	@Column(name = "SAVE_DATE")
	private LocalDateTime dateTime;
	
	@NotNull(message = "ARRAY BYTES IS REQUIRED.")
	@Column(name = "ARRAY_BYTES")
	private byte[] bytes;
	
	@NotNull(message = "GAME ID IS REQUIRED.")
	@ManyToOne
	@JoinColumn(name = "ID_GAME")
	private Game game;
	
	public Savegame() {
		
	}

	public Savegame(Long id, LocalDateTime date, byte[] bytes, Game game) {
		super();
		this.id = id;
		this.dateTime = date;
		this.bytes = bytes;
		this.game = game;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public LocalDateTime getDateTime() {
		return dateTime;
	}

	public void setDateTime(LocalDateTime dateTime) {
		this.dateTime = dateTime;
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
		Savegame other = (Savegame) obj;
		return Objects.equals(id, other.id);
	}
	
	

}
