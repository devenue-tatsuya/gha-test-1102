import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class HeroService {
  private url = 'http://127.0.0.1:5000';
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  constructor(private http: HttpClient) {}

  getHeroes() {
    return this.http.get<any>(`${this.url}/api/heroes`);
  }

  addHero(heroName: any): any {
    return this.http.post<any>(
      `${this.url}/api/heroes`,
      { name: heroName },
      this.httpOptions
    );
  }
}
