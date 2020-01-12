function cal(){
				var gr=document.getElementById("gr");
				var gw=document.getElementById("gw");
				var ge=document.getElementById("ge");
				var or=document.getElementById("or");
				var ow=document.getElementById("ow");
				var oe=document.getElementById("oe");
				var pr=document.getElementById("pr");
				var pw=document.getElementById("pw");
				var pe=document.getElementById("pe");
				var ocval=0;
				var symval="---------"
				if(gr.checked == true)
				{
					ocval+=40;
					var index = 3;
					symval = symval.substr(0, index) + 'r' + symval.substr(index + 1);
				}
				if(gw.checked == true)
				{
					ocval+=20;
					index = 4;
					symval = symval.substr(0, index) + 'w' + symval.substr(index + 1);
				}
				
				if(ge.checked == true)
				{
					ocval+=10;
					index = 5;
					symval = symval.substr(0, index) + 'x' + symval.substr(index + 1);
				}

				if(or.checked == true)
				{
					ocval+=400;
					index = 0;
					symval = symval.substr(0, index) + 'r' + symval.substr(index + 1);
				}
				if(ow.checked == true)
				{
					ocval+=200;
					index = 1;
					symval = symval.substr(0, index) + 'w' + symval.substr(index + 1);
				}

				if(oe.checked == true)
				{
					ocval+=100;
					index = 2;
					symval = symval.substr(0, index) + 'x' + symval.substr(index + 1);
				}
				
				if(pr.checked == true)
				{
					ocval+=4;
					index = 6;
					symval = symval.substr(0, index) + 'r' + symval.substr(index + 1);
				}
				if(pw.checked == true)
				{
					ocval+=2;
					index = 7;
					symval = symval.substr(0, index) + 'w' + symval.substr(index + 1);
				}
				if(pe.checked == true)
				{
					ocval+=1;
					index = 8;
					symval = symval.substr(0, index) + 'x' + symval.substr(index + 1);
				}
				
				document.getElementById("oc").value=ocval;
				document.getElementById("sym").value=symval;
			}