package rafaelribeiroestrela.com.github.backupgames.resources.exceptions;

import java.time.Instant;

import javax.servlet.http.HttpServletRequest;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import rafaelribeiroestrela.com.github.backupgames.services.exceptions.ApiException;

@ControllerAdvice
public class ResourceExceptionHandler {

	@ExceptionHandler(ApiException.class)
	public ResponseEntity<StandardError> ErroPersonalizado(ApiException e, HttpServletRequest request) {
		
		StandardError err = new StandardError();
		err.setTimestamp(Instant.now());
		err.setStatus(HttpStatus.BAD_REQUEST.value());
		err.setError(e.getMessage());
		err.setPath(request.getRequestURI());
		return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(err);
	}
	
}
