package rafaelribeiroestrela.com.github.backupgames.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import rafaelribeiroestrela.com.github.backupgames.models.SaveGame;

public interface SaveGameRepository extends JpaRepository<SaveGame, Long>{
	
	@Query("SELECT sv FROM SaveGame sv WHERE sv.game.id = :id")
	List<SaveGame> findByGameId(Long id);
	
	@Query("SELECT sv FROM SaveGame sv WHERE sv.game.id = :id ORDER BY sv.id DESC")
	List<SaveGame> findLastSaveGameByGameId(Long id);

}
