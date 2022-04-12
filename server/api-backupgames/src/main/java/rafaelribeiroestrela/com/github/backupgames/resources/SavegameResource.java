package rafaelribeiroestrela.com.github.backupgames.resources;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import rafaelribeiroestrela.com.github.backupgames.models.Savegame;
import rafaelribeiroestrela.com.github.backupgames.services.SavegameService;

@RestController
@RequestMapping("/savegames")
public class SavegameResource {
	
	@Autowired
	private SavegameService savegameService;
	
	
	@PostMapping
	public ResponseEntity<Savegame> save(@RequestBody Savegame savegame){
		return ResponseEntity.status(HttpStatus.CREATED).body(savegameService.save(savegame));
	}
	
	@GetMapping("all/game/{id}")
	public ResponseEntity<List<Savegame>> findByGameId(@PathVariable Long id){
		return ResponseEntity.status(HttpStatus.OK).body(savegameService.findByGameId(id));
	}
	
	@GetMapping("/lastsave/game/{id}")
	public ResponseEntity<Savegame> findLastSaveGameByGameId(@PathVariable Long id){
		return ResponseEntity.status(HttpStatus.OK).body(savegameService.findLastSaveGameByGameId(id));
	}
	


}
