package rafaelribeiroestrela.com.github.backupgames;

import java.time.LocalDateTime;
import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import rafaelribeiroestrela.com.github.backupgames.models.Game;
import rafaelribeiroestrela.com.github.backupgames.models.Savegame;
import rafaelribeiroestrela.com.github.backupgames.repositories.GameRepository;
import rafaelribeiroestrela.com.github.backupgames.repositories.SavegameRepository;

@SpringBootApplication
public class ApiBackupgamesApplication implements CommandLineRunner{
	
	@Value("${spring.profiles.active}")
	private String profile;
	
	@Autowired
	private GameRepository gameRepository;
	
	@Autowired
	private SavegameRepository savegameRepository;
	
	public static void main(String[] args) {
		SpringApplication.run(ApiBackupgamesApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		// TODO Auto-generated method stub
		
		if (profile.equals("test")) {
			Game g1 = new Game(null, "Call of Duty Modern Warfare");
			Game g2 = new Game(null, "Minecraft");
			Game g3 = new Game(null, "Need for Speed Underground 2");
			gameRepository.saveAll(Arrays.asList(g1, g2, g3));
			
			String bytes = "XPTO";
			Savegame s1 = new Savegame(null, LocalDateTime.now(), bytes.getBytes(), g1);
			Savegame s2 = new Savegame(null, LocalDateTime.now(), bytes.getBytes(), g1);
			
			
			savegameRepository.saveAll(Arrays.asList(s1, s2));
			
		}
		
	}
	
}
