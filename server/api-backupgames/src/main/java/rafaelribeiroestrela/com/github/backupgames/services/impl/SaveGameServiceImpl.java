package rafaelribeiroestrela.com.github.backupgames.services.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import rafaelribeiroestrela.com.github.backupgames.models.SaveGame;
import rafaelribeiroestrela.com.github.backupgames.repositories.SaveGameRepository;
import rafaelribeiroestrela.com.github.backupgames.services.SaveGameService;

@Service
public class SaveGameServiceImpl implements SaveGameService{
	
	@Autowired
	private SaveGameRepository saveGameRepository;

	@Override
	public SaveGame save(SaveGame obj) {
		return saveGameRepository.save(obj);
	}

	@Override
	public List<SaveGame> findByGameId(Long id) {
		return saveGameRepository.findByGameId(id);
	}

	@Override
	public SaveGame findLastSaveGameByGameId(Long id) {
		List<SaveGame> list = saveGameRepository.findLastSaveGameByGameId(id);
		return list.get(0);
	}


}
