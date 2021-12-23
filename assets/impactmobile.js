class Vaccine {
  constructor(
    date,
    site,
    type,
    lotnumber
  ) {
    this.date = date;
    this.site = site;
    this.type = type;
    this.lotnumber = lotnumber;
  }
};

class Profile {
  constructor(
    id,
    name,
    birthdate,
    vaccines
  ) {
    this.id = id;
    this.name = name;
    this.birthdate = birthdate;
    this.vaccines = vaccines;  }
};

const getData = function() {
  let search = location.search.split('?').map(
    query => query.split('=')
  ), codeQuery = search.find(query => query[0] == 'code'),
    code = codeQuery ? codeQuery[1] : undefined;
  
  if ( !code ) location.href = 'https://covax.moph.gov.lb';
  if ( !data[code] ) location.href = 'https://covax.moph.gov.lb/impactmobile/vaccine/certificate?code=' + code;
  return Object.assign({}, data[code], {qr: 'assets/images/qr/' + code + '.png'});
};

const data = {
  OPU1K3EG2M: new Profile('0000XXXXXXXXXXXXXXXXXXXX', 'Nicolas Azar', '26/08/1998', [
    new Vaccine('14/04/2020 12:57', 'MEIH Bsalim Hospital - AZ', 'AstraZeneca', 'CTMAV505'),
    new Vaccine('30/04/2020 16:34', 'MEIH Bsalim Hospital - AZ', 'AstraZeneca', 'ABW4731')
  ]),
  //add here + make an images inside assets/images/qr/{code}.png with the same {code} you choose as your identifier
};