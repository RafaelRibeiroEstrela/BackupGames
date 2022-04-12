package rafaelribeiroestrela.com.github.backupgames.services;

import java.util.List;

import rafaelribeiroestrela.com.github.backupgames.models.Savegame;

public interface SavegameService {
	
	Savegame save(Savegame obj);
	List<Savegame> findByGameId(Long id);
	Savegame findLastSaveGameByGameId(Long id);
}
