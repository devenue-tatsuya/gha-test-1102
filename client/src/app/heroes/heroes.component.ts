import { Component } from '@angular/core';
import { HeroService } from '../hero.service';
import { Heroes } from '../shared/types/heroes';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.scss'],
})
export class HeroesComponent {
  heroes: Heroes[] = [];

  constructor(private readonly heroService: HeroService) {}

  ngOnInit(): void {
    this.heroService.getHeroes().subscribe((response) => {
      this.heroes = response;
    });
  }
}
