package rafaelribeiroestrela.com.github.backupgames.services;

import java.util.List;

import rafaelribeiroestrela.com.github.backupgames.models.SaveGame;

public interface SaveGameService {
	
	SaveGame save(SaveGame obj);
	List<SaveGame> findByGameId(Long id);
	SaveGame findLastSaveGameByGameId(Long id);
}
