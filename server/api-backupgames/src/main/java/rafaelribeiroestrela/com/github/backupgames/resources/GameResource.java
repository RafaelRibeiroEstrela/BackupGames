package rafaelribeiroestrela.com.github.backupgames.resources;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import rafaelribeiroestrela.com.github.backupgames.models.Game;
import rafaelribeiroestrela.com.github.backupgames.services.GameService;

@RestController
@RequestMapping("/games")
public class GameResource {
	
	@Autowired
	private GameService gameService;
	
	@PostMapping
	public ResponseEntity<Game> save(@RequestBody Game obj){
		return ResponseEntity.status(HttpStatus.CREATED).body(gameService.save(obj));
	}
	
	@GetMapping
	public ResponseEntity<List<Game>> findAll(){
		return ResponseEntity.status(HttpStatus.OK).body(gameService.findAll());
	}

}
