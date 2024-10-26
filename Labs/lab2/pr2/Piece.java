package lab2.pr2;

abstract class Piece {
	protected String name; 
	protected String color; 
	
	public Piece() { 
	}
	
	public Piece(String name, String color) { 
		this.name = name; 
		this.color=color; 
	}
	
	public abstract boolean isLegalMove(Position a, Position b); 
	
	
	public void setName() { 
		this.name =name;
	}
	
	public void setColor() { 
		this.color= color; 
	}
	public String getColor () { 
		return color; 
		
	}
	public String getName() { 
		return name; 
	}
	
}