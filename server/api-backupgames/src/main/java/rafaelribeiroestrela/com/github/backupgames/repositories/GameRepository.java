package rafaelribeiroestrela.com.github.backupgames.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import rafaelribeiroestrela.com.github.backupgames.models.Game;

public interface GameRepository extends JpaRepository<Game, Long>{

}
