package rafaelribeiroestrela.com.github.backupgames.services.impl;

import java.time.LocalDateTime;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import rafaelribeiroestrela.com.github.backupgames.models.Savegame;
import rafaelribeiroestrela.com.github.backupgames.repositories.SavegameRepository;
import rafaelribeiroestrela.com.github.backupgames.services.SavegameService;

@Service
public class SavegameServiceImpl implements SavegameService{
	
	@Autowired
	private SavegameRepository saveGameRepository;

	@Override
	public Savegame save(Savegame obj) {
		obj.setDateTime(LocalDateTime.now());
		return saveGameRepository.save(obj);
	}

	@Override
	public List<Savegame> findByGameId(Long id) {
		return saveGameRepository.findByGameId(id);
	}

	@Override
	public Savegame findLastSaveGameByGameId(Long id) {
		List<Savegame> list = saveGameRepository.findLastSaveGameByGameId(id);
		return list.get(0);
	}


}
