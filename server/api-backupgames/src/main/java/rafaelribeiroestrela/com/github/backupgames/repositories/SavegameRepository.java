package rafaelribeiroestrela.com.github.backupgames.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import rafaelribeiroestrela.com.github.backupgames.models.Savegame;

public interface SavegameRepository extends JpaRepository<Savegame, Long>{
	
	@Query("SELECT sv FROM Savegame sv WHERE sv.game.id = :id")
	List<Savegame> findByGameId(Long id);
	
	@Query("SELECT MAX(sv) FROM Savegame sv WHERE sv.game.id = :id")
	List<Savegame> findLastSaveGameByGameId(Long id);

}
