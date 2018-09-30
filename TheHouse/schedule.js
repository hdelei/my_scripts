/**
 * @file Get The House Schedule Details
 * @author Vanderlei Mendes 
 * @version 1.0
 * @description Alert Popup with detailed information from checked classes 
 */


//Get all divs based in bgcolor
var rows = $('a').filter(function(){
    var color = $(this).css("background-color").toLowerCase();
    return color === "rgb(28, 77, 134)" ;
});

var eventList = 
{
    'aula':[], 
    'data':[], 
    'sala':[], 
    'professor':[],
    'alunos':[] 
};

var ex = $.expando + "2";

for(i = 0; i < rows.length; i++){
    eventList.aula.push(rows[i][ex].fcSeg.event.aula);
    eventList.data.push(rows[i][ex].fcSeg.event.start._i);
    eventList.sala.push(rows[i][ex].fcSeg.event.sala);
    eventList.professor.push(rows[i][ex].fcSeg.event.professor);
    eventList.alunos.push(rows[i][ex].fcSeg.event.numAlunos);

    var temp = 'Aula: ' + eventList.aula[i] + '\n';
    temp += 'Data: ' + new Date(eventList.data[i]).toLocaleDateString('pt-br');
    temp += ' Hora: ' + eventList.data[i].substring(11, 16) + '\n'
    temp += 'Sala: ' + eventList.sala[i] + '\n';
    temp += 'Professor: ' + eventList.professor[i] + '\n';
    temp += 'Número de alunos: ' + eventList.alunos[i];

    alert(temp);    
}

