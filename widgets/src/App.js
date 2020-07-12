import React, { useState } from 'react';
import Accordion from './components/Accordion';
import Search from './components/Search';
import Dropdown from './components/Dropdown';
import Translate from './components/Translate';
import Route from './components/Route';
import Header from './components/Header';

const items = [
    {
        title: 'What is React?',
        content: '48 years jowabella Cholo sangkatuts valaj wrangler waz sangkatuts sa at bakit ano krung-krung jongoloids at ng ang at nang keme ang ng ganders otoko daki at jongoloids sa ng bakit shonga-shonga valaj tanders.'
    },
    {
        title: 'Why use react?',
        content: 'ano cheapangga jupang-pang ugmas bigalou 48 years planggana lulu pranella bokot effem urky at nang bigalou conalei shonga at nang quality control urky ng pamenthol ang wiz tungril ng chipipay Mike , bakit urky cheapangga tamalis nang bokot chaka ng at ang pamin kasi intonses ganda lang.'
    },
    {
        title: 'How do you use React?',
        content: 'daki conalei chopopo chapter bella cheapangga intonses , sa oblation sa krung-krung ganda lang majonders makyonget kemerloo kasi katagalugan na jupang-pang shonget sudems ang.'

    }
];

const options = [
    {
        label: "The colour red",
        colour: "red"
    },
    {
        label: "The colour green",
        colour: "green"
    },
    {
        label: "A shade of blue",
        colour: "blue"
    },
];

export default () => {
    const [selected, setSelected]=useState(options[0]);

    return (
        <div>
            <Header />
            <Route path="/">
                <Accordion items={items} />
            </Route>
            <Route path="/list">
                <Search />
            </Route>
            <Route path="/dropdown">
                <Dropdown  
                    label="Select a color"
                    options={options}
                    selected={selected}
                    onSelectedChange={setSelected}
                />
            </Route>
            <Route path="/translate">
                <Translate  />
            </Route>
        </div>
    );
}