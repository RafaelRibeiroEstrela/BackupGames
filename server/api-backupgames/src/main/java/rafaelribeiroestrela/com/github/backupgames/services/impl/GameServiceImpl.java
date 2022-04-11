package rafaelribeiroestrela.com.github.backupgames.services.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import rafaelribeiroestrela.com.github.backupgames.models.Game;
import rafaelribeiroestrela.com.github.backupgames.repositories.GameRepository;
import rafaelribeiroestrela.com.github.backupgames.services.GameService;

@Service
public class GameServiceImpl implements GameService{

	@Autowired
	private GameRepository gameRepository;
	
	@Override
	public Game save(Game obj) {
		return gameRepository.save(obj);
	}

	@Override
	public List<Game> findAll() {
		return gameRepository.findAll();
	}

}
