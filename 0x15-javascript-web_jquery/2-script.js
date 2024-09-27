const $ = window.$;

const header = $('header');
const divRedHeader = $('div#red_header');

divRedHeader.on('click', () => header.css('colour', '#FF0000'));
