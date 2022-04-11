package rafaelribeiroestrela.com.github.backupgames.services;

import java.util.List;

import rafaelribeiroestrela.com.github.backupgames.models.Game;

public interface GameService {
	
	Game save(Game obj);
	List<Game> findAll();

}
