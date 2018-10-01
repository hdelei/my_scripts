/**
 * @file Get The House Schedule Details
 * @author Vanderlei Mendes 
 * @version 1.1
 * @description Alert Popup with detailed information from checked classes 
 * 
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

$('#myModal').modal();
$('#modalBody').html('');
$('#modalTitle').html('The House Schedule Summary');
$('#botaoModal').hide();

//var qrText = '';
for(i = 0; i < rows.length; i++){
    eventList.aula.push(rows[i][ex].fcSeg.event.aula);
    eventList.data.push(rows[i][ex].fcSeg.event.start._i);
    eventList.sala.push(rows[i][ex].fcSeg.event.sala);
    eventList.professor.push(rows[i][ex].fcSeg.event.professor);
    eventList.alunos.push(rows[i][ex].fcSeg.event.numAlunos);

    var temp = '<strong>Aula</strong>: ' + eventList.aula[i] + '<br>';
    temp += '<strong>Data</strong>: ' + new Date(eventList.data[i]).toLocaleDateString('pt-br');
    temp += '<strong>Hora</strong>: ' + eventList.data[i].substring(11, 16) + '<br>'
    temp += '<strong>Sala</strong>: ' + eventList.sala[i] + '<br>';
    temp += '<strong>Professor</strong>: ' + eventList.professor[i] + '<br>';
    temp += '<strong>Número de alunos</strong>: ' + eventList.alunos[i] + '<p>';    
    
    $('#modalBody').append(temp);
    //qrText += temp;
}

/*QRCode part not implemented yet*/

// $('body').append('<script type="text/javascript" src="http://davidshimjs.github.com/qrcodejs/qrcode.min.js"></script>');

// qrText.replace(/<br>|<p>/g, '\n');
// qrText.replace(/<strong>|<\/strong>/g, '');

// var qrcode = new QRCode("modalBody");
// qrcode.makeCode(qrText);