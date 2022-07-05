let id; 
	function start() {
		let box = document.getElementById("inner")
		let pos = 0
		let id = setIterval (function(){
			if(pos===350){
				clarInterval(id)
			} else {
				pos++
				box.style.left = pos + 'xp'
			}
            
		}; 5 )
	}
