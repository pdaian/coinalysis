from graphs import graphs

from graphs import num_simple_and_complex_gather, num_simple_and_complex_draw
#graphs.gather_data(1, 438746, 'graphs/data/num_simple_and_complex', num_simple_and_complex_gather)
#num_simple_and_complex_draw.draw('graphs/data/num_simple_and_complex')

from graphs import processing_time_gather, processing_time_draw
#graphs.gather_data(1, 438746, 'graphs/data/processing_time', processing_time_gather)
#processing_time_draw.draw('graphs/data/processing_time')

from graphs import all_amounts_gather, all_amounts_draw, all_amounts_multiple
#graphs.gather_data(1, 438746, 'graphs/data/all_amounts', all_amounts_gather)
#graphs.gather_data(400000, 438746, 'graphs/data/recent_amounts', all_amounts_gather)
#all_amounts_draw.draw('graphs/data/all_amounts')
#all_amounts_draw.draw('graphs/data/recent_amounts', color='green')


from graphs import anonymity_gather, anonymity_draw
#graphs.gather_data(1, 438746, 'graphs/data/anonymity', anonymity_gather)
anonymity_draw.draw('graphs/data/anonymity')
