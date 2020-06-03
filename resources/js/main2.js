const {google} = require('googleapis'); 
const keys = require('./google-keys.json');


const client = new google.auth.JWT(
    keys.client_email, 
    null, 
    keys.private_key,
    ['https://www.googleapis.com/auth/spreadsheets']
);

client.authorize(function(err, tokens){
    if (err){
        console.log(err);
        return;
    } 
    else{
        console.log('Connected');
        gsrun(client);
    }
});

async function gsrun(client){

    const gsapi = google.sheets({version:'v4', auth: client});

    const opt ={
        spreadsheetId: '1K7_xu13Ri1MHUT5pFEn4Ga6E3wy-njH2NxIlp3UfLW4',
        range: 'A2:H4'
    };

    let data = await gsapi.spreadsheets.values.get(opt);
    let dataArray = data.data.values;

    console.log(dataArray);

    const updateOptions = {
        spreadsheetId: '1K7_xu13Ri1MHUT5pFEn4Ga6E3wy-njH2NxIlp3UfLW4',
        range: 'E2',
        valueInputOption: 'USER_ENTERED',
        resource: {values: dataArray}
    }

    let res = await gsapi.spreadsheets.values.update(updateOptions);

    console.log(res);
}