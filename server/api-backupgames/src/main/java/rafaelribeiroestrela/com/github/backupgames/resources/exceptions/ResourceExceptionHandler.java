package rafaelribeiroestrela.com.github.backupgames.resources.exceptions;

import java.time.LocalDateTime;

import javax.servlet.http.HttpServletRequest;
import javax.validation.ConstraintViolationException;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import rafaelribeiroestrela.com.github.utilidades.exceptions.ApiException;
import rafaelribeiroestrela.com.github.utilidades.exceptions.StandardError;

@ControllerAdvice
public class ResourceExceptionHandler {
	
	@ExceptionHandler(ApiException.class)
	public ResponseEntity<StandardError> CustomError(ApiException e, HttpServletRequest request) {
		
		StandardError err = new StandardError();
		err.setTime(LocalDateTime.now());
		err.setStatus(HttpStatus.BAD_REQUEST.value());
		err.setError(e.getMessage());
		err.setPath(request.getRequestURI());
		return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(err);
	}
	
	@ExceptionHandler(ConstraintViolationException.class)
	public ResponseEntity<StandardError> CustomError(ConstraintViolationException e, HttpServletRequest request) {
		StandardError err = new StandardError();
		err.setTime(LocalDateTime.now());
		err.setStatus(HttpStatus.BAD_REQUEST.value());
		err.setError(getMessageTemplate(e));
		err.setPath(request.getRequestURI());
		return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(err);
	}
	
	private String getMessageTemplate(ConstraintViolationException e) {
		String msg = e.getLocalizedMessage();
		int index = msg.indexOf("messageTemplate");
		String temp = "";
		boolean start = false;
		while(true) {
			char c = msg.charAt(index);
			if (c == '}') {
				break;
			}
			if (start) {
				temp += c;
			}
			if (c == '=') {
				start = true;
			}
			index += 1;
		}
		return temp;
	}

}
